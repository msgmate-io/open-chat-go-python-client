import argparse
import json
import time
from dataclasses import dataclass
from typing import Any, Optional
from urllib.parse import urlparse

from .generated_api import Client as GeneratedClient
from .generated_api.api.chats import (
    get_api_v1_chats_chat_uuid,
    get_api_v1_chats_list,
    post_api_chat_chat_uuid_publish,
    post_api_v1_chats_create,
)
from .generated_api.api.contacts import get_api_v1_contacts_contact_token, get_api_v1_contacts_list
from .generated_api.api.messages import get_api_v1_chats_chat_uuid_messages_list
from .generated_api.api.user import post_api_v1_user_login
from .generated_api.api.users import get_api_v1_user_self
from .generated_api.models.chats_create_chat import ChatsCreateChat
from .generated_api.models.chats_create_chat_shared_config import ChatsCreateChatSharedConfig
from .generated_api.models.chats_listed_chat import ChatsListedChat
from .generated_api.models.chats_listed_chats_page import ChatsListedChatsPage
from .generated_api.models.chats_listed_message import ChatsListedMessage
from .generated_api.models.chats_listed_messages_page import ChatsListedMessagesPage
from .generated_api.models.chats_shared_chat_publish_response import ChatsSharedChatPublishResponse
from .generated_api.models.contacts_listed_contact import ContactsListedContact
from .generated_api.models.contacts_paginated_contacts import ContactsPaginatedContacts
from .generated_api.models.database_user import DatabaseUser
from .generated_api.models.user_user_login import UserUserLogin
from .generated_api.types import UNSET, Unset


DEFAULT_BOT_CONFIG: dict[str, Any] = {
    "temperature": 0.7,
    "max_tokens": 4096,
    "model": "qwen3-8b-instruct_vllm",
    "endpoint": "https://litellm.t1m.me/v1",
    "backend": "litellm",
    "context": 10,
    "system_prompt": "You are a helpful assistant.",
}

Interaction = ChatsListedChat
InteractionsPage = ChatsListedChatsPage
Message = ChatsListedMessage
MessagesPage = ChatsListedMessagesPage


@dataclass
class PasswordAuth:
    email: str
    password: str


@dataclass
class TokenAuth:
    token: str


@dataclass
class InteractionStopSignal:
    chat_uuid: str
    reason: str
    latest_message_uuid: str | None = None


@dataclass
class InteractionConfirmation:
    action_id: str
    source_tool_name: str | None = None
    tool_input: dict[str, Any] | None = None
    tool_call_arguments: dict[str, Any] | None = None
    suggested_inputs: Any = None


def _is_unset(value: Any) -> bool:
    return isinstance(value, Unset)


def _as_str(value: Any) -> str:
    return "" if _is_unset(value) or value is None else str(value)


def _expect_ok(parsed: Any, status_code: int, context: str) -> Any:
    if status_code >= 400:
        raise RuntimeError(f"{context} failed with status {status_code}")
    if parsed is None or isinstance(parsed, str):
        raise RuntimeError(f"{context} failed with unexpected payload type {type(parsed)!r}")
    return parsed


class InteractionSession:
    def __init__(self, client: "OpenChatClient", interaction: Interaction):
        self._client = client
        self._interaction = interaction

    @property
    def data(self) -> Interaction:
        return self._interaction

    @property
    def uuid(self) -> str:
        value = self._interaction.uuid
        if _is_unset(value):
            raise RuntimeError("interaction has no uuid")
        return value

    def refresh(self) -> Interaction:
        self._interaction = self._client.get_interaction(self.uuid)
        return self._interaction

    def messages(self, page: int = 1, limit: int = 40) -> MessagesPage:
        return self._client.list_interaction_messages(self.uuid, page=page, limit=limit)

    def wait_until_finished(
        self,
        timeout_seconds: int = 20,
        poll_interval: float = 0.5,
        quiet_seconds: float = 3.0,
    ) -> Message | InteractionStopSignal:
        return self._client.wait_for_interaction(
            self.uuid,
            timeout_seconds=timeout_seconds,
            poll_interval=poll_interval,
            quiet_seconds=quiet_seconds,
        )

    def confirmations(self, wait_seconds: int = 10, poll_interval: float = 0.5) -> list[InteractionConfirmation]:
        return self._client.get_interaction_confirmations(self.uuid, wait_seconds=wait_seconds, poll_interval=poll_interval)

    def execute_confirmation(
        self,
        message_uuid: str,
        action_id: str,
        continue_after_execute: bool = True,
    ) -> dict[str, Any]:
        return self._client.execute_confirm_action(
            chat_uuid=self.uuid,
            message_uuid=message_uuid,
            action_id=action_id,
            continue_after_execute=continue_after_execute,
        )

    def publish(self) -> ChatsSharedChatPublishResponse:
        return self._client.publish_chat(self.uuid)

    def shared_url(self) -> str:
        return self._client.get_shared_interaction_url(self.uuid)


class Bot:
    def __init__(self, client: "OpenChatClient", contact: ContactsListedContact):
        self._client = client
        self._contact = contact
        self._resolved_profile: ContactsListedContact | None = None

    @property
    def contact(self) -> ContactsListedContact:
        return self._contact

    @property
    def uuid(self) -> str:
        return _as_str(self._contact.user_uuid)

    @property
    def name(self) -> str:
        return _as_str(self._contact.name)

    @property
    def contact_token(self) -> str:
        token = _as_str(self._contact.contact_token)
        if not token:
            raise RuntimeError("bot is missing contact_token")
        return token

    def refresh(self) -> ContactsListedContact:
        response = get_api_v1_contacts_contact_token.sync_detailed(contact_token=self.contact_token, client=self._client._api)
        parsed = _expect_ok(response.parsed, int(response.status_code), "bot refresh")
        if not isinstance(parsed, ContactsListedContact):
            raise RuntimeError(f"bot refresh returned unexpected type: {type(parsed)!r}")
        self._resolved_profile = parsed
        self._contact = parsed
        return parsed

    def default_config(self) -> dict[str, Any]:
        if self._resolved_profile is None:
            self.refresh()
        profile = self._resolved_profile
        if profile is None or _is_unset(profile.profile_data):
            return dict(DEFAULT_BOT_CONFIG)

        profile_data = profile.profile_data.additional_properties
        models = profile_data.get("models")
        if isinstance(models, list):
            for model in models:
                if not isinstance(model, dict):
                    continue
                config = model.get("configuration")
                if isinstance(config, dict):
                    resolved = dict(DEFAULT_BOT_CONFIG)
                    resolved.update(config)
                    return resolved
        return dict(DEFAULT_BOT_CONFIG)

    def create_interaction(
        self,
        message: str,
        tool_init: Optional[dict[str, Any]] = None,
        overrides: Optional[dict[str, Any]] = None,
    ) -> InteractionSession:
        return self._client.create_interaction_for_bot(
            bot=self,
            message=message,
            tool_init=tool_init,
            overrides=overrides,
        )


class OpenChatClient:
    def __init__(
        self,
        base_url: str = "http://localhost:1984",
        host: str | None = None,
        auth: PasswordAuth | TokenAuth | None = None,
        username: str = "admin",
        password: str = "password",
        api_token: str | None = None,
    ):
        resolved_base_url = (host or base_url).rstrip("/")
        self.base_url = resolved_base_url
        if auth is None:
            if api_token:
                auth = TokenAuth(token=api_token)
            else:
                auth = PasswordAuth(email=username, password=password)
        self._auth = auth
        self._logged_in = isinstance(auth, TokenAuth)
        self._last_chat_uuid: str | None = None
        self._default_interaction_overrides: dict[str, Any] = {}

        headers = {"Content-Type": "application/json", "Origin": self.base_url}
        if isinstance(auth, TokenAuth):
            headers["Authorization"] = f"Bearer {auth.token}"

        self._api = GeneratedClient(
            base_url=self.base_url,
            headers=headers,
            follow_redirects=True,
            raise_on_unexpected_status=False,
        )

    def _cookie_domain(self) -> str:
        parsed = urlparse(self.base_url)
        return parsed.hostname or ""

    def login(self) -> DatabaseUser:
        if self._logged_in:
            return self.me()
        if not isinstance(self._auth, PasswordAuth):
            raise RuntimeError("password auth required for login")
        response = post_api_v1_user_login.sync_detailed(
            client=self._api,
            body=UserUserLogin(email=self._auth.email, password=self._auth.password),
            cookie_domain=self._cookie_domain(),
        )
        _expect_ok(response.parsed, int(response.status_code), "login")
        self._logged_in = True
        return self.me()

    def ensure_authenticated(self) -> None:
        if not self._logged_in:
            self.login()

    def me(self) -> DatabaseUser:
        self.ensure_authenticated()
        response = get_api_v1_user_self.sync_detailed(client=self._api)
        parsed = _expect_ok(response.parsed, int(response.status_code), "me")
        if not isinstance(parsed, DatabaseUser):
            raise RuntimeError(f"me returned unexpected type: {type(parsed)!r}")
        return parsed

    def get_user_self(self) -> DatabaseUser:
        return self.me()

    def list_bots(self, page_size: int = 100) -> list[Bot]:
        self.ensure_authenticated()
        page = 1
        bots: list[Bot] = []
        while True:
            response = get_api_v1_contacts_list.sync_detailed(client=self._api, page=page, limit=page_size)
            parsed = _expect_ok(response.parsed, int(response.status_code), "list_bots")
            if not isinstance(parsed, ContactsPaginatedContacts):
                raise RuntimeError(f"list_bots returned unexpected type: {type(parsed)!r}")
            rows = [] if _is_unset(parsed.rows) else parsed.rows
            for row in rows:
                if not _is_unset(row.is_automated) and row.is_automated:
                    bots.append(Bot(client=self, contact=row))
            total_pages = 1 if _is_unset(parsed.total_pages) else int(parsed.total_pages)
            if page >= total_pages:
                break
            page += 1
        return bots

    def setup_bot_config(self, bot_config: dict[str, Any]) -> None:
        self._default_interaction_overrides = dict(bot_config)

    def get_bot(self, identifier: str) -> Bot:
        if not identifier.strip():
            raise ValueError("bot identifier is required")
        bots = self.list_bots()
        matches = []
        needle = identifier.strip()
        for bot in bots:
            if bot.uuid == needle or bot.name == needle or bot.contact_token == needle:
                matches.append(bot)
        if not matches:
            raise RuntimeError(f"bot not found: {identifier}")
        if len(matches) > 1:
            options = ", ".join(f"{bot.name} ({bot.uuid})" for bot in matches)
            raise RuntimeError(f"ambiguous bot identifier '{identifier}': {options}")
        return matches[0]

    def create_interaction_for_bot(
        self,
        bot: Bot,
        message: str,
        tool_init: Optional[dict[str, Any]] = None,
        overrides: Optional[dict[str, Any]] = None,
    ) -> InteractionSession:
        self.ensure_authenticated()
        effective_config = bot.default_config()
        effective_config.update(self._default_interaction_overrides)
        if overrides:
            effective_config.update(overrides)
        effective_config["tool_init"] = tool_init or {}

        body = ChatsCreateChat(
            contact_token=bot.contact_token,
            first_message=message,
            chat_type="interaction",
            shared_config=ChatsCreateChatSharedConfig.from_dict(effective_config),
        )
        response = post_api_v1_chats_create.sync_detailed(client=self._api, body=body)
        parsed = _expect_ok(response.parsed, int(response.status_code), "create_interaction_for_bot")
        if not isinstance(parsed, ChatsListedChat):
            raise RuntimeError(f"create_interaction_for_bot returned unexpected type: {type(parsed)!r}")
        if not _is_unset(parsed.chat_type) and not str(parsed.chat_type).startswith("interaction"):
            raise RuntimeError(f"create_interaction_for_bot returned non-interaction chat_type: {parsed.chat_type}")
        if not _is_unset(parsed.uuid):
            self._last_chat_uuid = parsed.uuid
        return InteractionSession(client=self, interaction=parsed)

    def create_interaction(
        self,
        tool_init: Optional[dict[str, Any]] = None,
        message: str = "",
    ) -> Interaction:
        interaction = self.get_bot("bot").create_interaction(
            message=message,
            tool_init=tool_init,
        )
        return interaction.data

    def list_interactions(self, page: int = 1, limit: int = 40, all_pages: bool = True) -> InteractionsPage:
        self.ensure_authenticated()
        response = get_api_v1_chats_list.sync_detailed(client=self._api, page=page, limit=limit, chat_types="interaction")
        parsed = _expect_ok(response.parsed, int(response.status_code), "list_interactions")
        if not isinstance(parsed, ChatsListedChatsPage):
            raise RuntimeError(f"list_interactions returned unexpected type: {type(parsed)!r}")
        if not all_pages or _is_unset(parsed.rows) or _is_unset(parsed.total_pages):
            return parsed
        total_pages = int(parsed.total_pages)
        merged_rows = list(parsed.rows)
        for next_page in range(page + 1, total_pages + 1):
            next_response = get_api_v1_chats_list.sync_detailed(
                client=self._api,
                page=next_page,
                limit=limit,
                chat_types="interaction",
            )
            next_parsed = _expect_ok(next_response.parsed, int(next_response.status_code), "list_interactions page")
            if not isinstance(next_parsed, ChatsListedChatsPage):
                raise RuntimeError(f"list_interactions page returned unexpected type: {type(next_parsed)!r}")
            if _is_unset(next_parsed.rows):
                continue
            merged_rows.extend(next_parsed.rows)
        return ChatsListedChatsPage(
            limit=parsed.limit,
            page=parsed.page,
            total_pages=parsed.total_pages,
            rows=merged_rows,
        )

    def get_interactions(self, page: int = 1, limit: int = 40, all_pages: bool = True) -> InteractionsPage:
        return self.list_interactions(page=page, limit=limit, all_pages=all_pages)

    def get_interaction(self, chat_uuid: str) -> Interaction:
        self.ensure_authenticated()
        response = get_api_v1_chats_chat_uuid.sync_detailed(client=self._api, chat_uuid=chat_uuid)
        parsed = _expect_ok(response.parsed, int(response.status_code), "get_interaction")
        if not isinstance(parsed, ChatsListedChat):
            raise RuntimeError(f"get_interaction returned unexpected type: {type(parsed)!r}")
        return parsed

    def interaction(self, chat_uuid: str) -> InteractionSession:
        return InteractionSession(client=self, interaction=self.get_interaction(chat_uuid))

    def list_interaction_messages(self, chat_uuid: str, page: int = 1, limit: int = 40) -> MessagesPage:
        self.ensure_authenticated()
        response = get_api_v1_chats_chat_uuid_messages_list.sync_detailed(
            chat_uuid=chat_uuid,
            client=self._api,
            page=page,
            limit=limit,
        )
        parsed = _expect_ok(response.parsed, int(response.status_code), "list_interaction_messages")
        if not isinstance(parsed, ChatsListedMessagesPage):
            raise RuntimeError(f"list_interaction_messages returned unexpected type: {type(parsed)!r}")
        return parsed

    def wait_for_interaction(
        self,
        chat_uuid: str,
        timeout_seconds: int = 20,
        poll_interval: float = 0.5,
        quiet_seconds: float = 3.0,
    ) -> Message | InteractionStopSignal:
        deadline = time.time() + max(timeout_seconds, 0)
        last_signature = ""
        last_change_at = time.time()
        latest_row: Message | None = None
        while True:
            payload = self.list_interaction_messages(chat_uuid=chat_uuid, page=1, limit=100)
            rows = [] if _is_unset(payload.rows) else payload.rows
            signature_parts: list[str] = []
            for row in rows:
                latest_row = row
                signature_parts.append(f"{_as_str(row.uuid)}|{_as_str(row.send_at)}|{_as_str(row.text)}")
                if not _is_unset(row.meta_data) and row.meta_data.additional_properties.get("finished") is True:
                    return row
            signature = "\n".join(signature_parts)
            now = time.time()
            if signature != last_signature:
                last_signature = signature
                last_change_at = now
            elif now - last_change_at >= max(quiet_seconds, 0.5):
                return InteractionStopSignal(
                    chat_uuid=chat_uuid,
                    reason=f"no message updates for {quiet_seconds:.1f}s",
                    latest_message_uuid=None if latest_row is None else _as_str(latest_row.uuid) or None,
                )
            if time.time() >= deadline:
                raise TimeoutError(f"interaction did not emit a stop signal within {timeout_seconds}s")
            time.sleep(max(poll_interval, 0.1))

    def interaction_wait_for_stop_signal(
        self,
        chat_uuid: Optional[str] = None,
        wait_seconds: int = 20,
        poll_interval: float = 0.5,
        quiet_seconds: float = 3.0,
    ) -> Message | InteractionStopSignal:
        target_chat_uuid = chat_uuid or self._last_chat_uuid
        if not target_chat_uuid:
            raise ValueError("chat_uuid is required when no interaction has been created yet")
        return self.wait_for_interaction(
            target_chat_uuid,
            timeout_seconds=wait_seconds,
            poll_interval=poll_interval,
            quiet_seconds=quiet_seconds,
        )

    def get_interaction_confirmations(
        self,
        chat_uuid: str,
        wait_seconds: int = 10,
        poll_interval: float = 0.5,
    ) -> list[InteractionConfirmation]:
        deadline = time.time() + max(wait_seconds, 0)
        while True:
            payload = self.list_interaction_messages(chat_uuid=chat_uuid, page=1, limit=100)
            rows = [] if _is_unset(payload.rows) else payload.rows
            action_by_id: dict[str, InteractionConfirmation] = {}
            has_finished_message = False
            for message in rows:
                meta_data = {} if _is_unset(message.meta_data) else message.meta_data.additional_properties
                if meta_data.get("finished") is True:
                    has_finished_message = True
                actions = meta_data.get("confirmable_actions")
                if isinstance(actions, list):
                    for action in actions:
                        if isinstance(action, dict):
                            action_id = str(action.get("action_id", "")).strip()
                            if action_id:
                                action_by_id[action_id] = InteractionConfirmation(action_id=action_id)
                if _is_unset(message.tool_calls):
                    continue
                for tool_call in message.tool_calls:
                    if not isinstance(tool_call, dict):
                        continue
                    action_id = str(tool_call.get("id", "")).strip()
                    if not action_id:
                        continue
                    confirmation = action_by_id.get(action_id, InteractionConfirmation(action_id=action_id))
                    confirmation_meta = tool_call.get("confirmation")
                    if isinstance(confirmation_meta, dict):
                        if isinstance(confirmation_meta.get("tool_input"), dict):
                            confirmation.tool_input = dict(confirmation_meta["tool_input"])
                        tool_name = confirmation_meta.get("tool_name")
                        if isinstance(tool_name, str) and tool_name:
                            confirmation.source_tool_name = tool_name
                    if isinstance(tool_call.get("arguments"), dict):
                        confirmation.tool_call_arguments = dict(tool_call["arguments"])
                    action_by_id[action_id] = confirmation
            if action_by_id:
                return list(action_by_id.values())
            if has_finished_message or time.time() >= deadline:
                return []
            time.sleep(max(poll_interval, 0.1))

    def get_interaction_confirmation_list(
        self,
        chat_uuid: str,
        wait_seconds: int = 10,
        poll_interval: float = 0.5,
    ) -> list[InteractionConfirmation]:
        return self.get_interaction_confirmations(chat_uuid, wait_seconds=wait_seconds, poll_interval=poll_interval)

    def execute_confirm_action(
        self,
        chat_uuid: str,
        message_uuid: str,
        action_id: str,
        continue_after_execute: bool = True,
    ) -> dict[str, Any]:
        self.ensure_authenticated()
        response = self._api.get_httpx_client().post(
            f"/api/v1/chats/{chat_uuid}/messages/{message_uuid}/confirm-actions/{action_id}/execute",
            json={"continue_after_execute": continue_after_execute},
        )
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise RuntimeError("execute_confirm_action returned non-object response")
        return payload

    def publish_chat(self, chat_uuid: str) -> ChatsSharedChatPublishResponse:
        self.ensure_authenticated()
        response = post_api_chat_chat_uuid_publish.sync_detailed(client=self._api, chat_uuid=chat_uuid)
        parsed = _expect_ok(response.parsed, int(response.status_code), "publish_chat")
        if not isinstance(parsed, ChatsSharedChatPublishResponse):
            raise RuntimeError(f"publish_chat returned unexpected type: {type(parsed)!r}")
        return parsed

    def get_shared_interaction_url(self, chat_uuid: str) -> str:
        published = self.publish_chat(chat_uuid)
        share_uuid = _as_str(published.chat_share_uuid)
        if not share_uuid:
            raise RuntimeError("publish endpoint did not return chat_share_uuid")
        return f"{self.base_url}/interaction/{share_uuid}"


# Alias for previous class name.
OpenChatPythonClient = OpenChatClient


def main() -> None:
    parser = argparse.ArgumentParser(description="Open-Chat Python client")
    parser.add_argument("--host", default="http://localhost:1984")
    parser.add_argument("--username", default="admin")
    parser.add_argument("--password", default="password")
    parser.add_argument("--api-token", default="")
    parser.add_argument("--bot", default="bot")
    parser.add_argument("--message", default="Hello from open_chat_client_python")
    args = parser.parse_args()

    auth = TokenAuth(args.api_token) if args.api_token else PasswordAuth(args.username, args.password)
    client = OpenChatClient(base_url=args.host, auth=auth)
    user = client.me() if args.api_token else client.login()
    print(f"Logged in as: {_as_str(user.name) or 'unknown'}")

    bot = client.get_bot(args.bot)
    interaction = bot.create_interaction(message=args.message)
    print(f"Created interaction chat: {interaction.uuid}")


if __name__ == "__main__":
    main()
