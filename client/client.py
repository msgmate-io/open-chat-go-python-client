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
from .generated_api.api.contacts import get_api_v1_contacts_list
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


def _expect_ok(parsed: Any, status_code: int, context: str) -> Any:
    if status_code >= 400:
        raise RuntimeError(f"{context} failed with status {status_code}")
    if parsed is None or isinstance(parsed, str):
        raise RuntimeError(f"{context} failed with unexpected payload type {type(parsed)!r}")
    return parsed


class OpenChatPythonClient:
    def __init__(
        self,
        host: str = "http://localhost:1984",
        username: str = "admin",
        password: str = "password",
        api_token: Optional[str] = None,
    ):
        self.host = host.rstrip("/")
        self.username = username
        self.password = password
        self.api_token = api_token
        self.bot_config = dict(DEFAULT_BOT_CONFIG)
        self._logged_in = api_token is not None
        self._last_chat_uuid: Optional[str] = None

        headers = {"Content-Type": "application/json", "Origin": self.host}
        if api_token:
            headers["Authorization"] = f"Bearer {api_token}"

        self._api_client = GeneratedClient(
            base_url=self.host,
            headers=headers,
            follow_redirects=True,
            raise_on_unexpected_status=False,
        )

    def _cookie_domain(self) -> str:
        parsed = urlparse(self.host)
        return parsed.hostname or ""

    def setup_bot_config(self, bot_config: dict[str, Any]) -> None:
        self.bot_config = dict(bot_config)

    def login(self) -> DatabaseUser:
        if self._logged_in:
            return self.get_user_self()

        response = post_api_v1_user_login.sync_detailed(
            client=self._api_client,
            body=UserUserLogin(email=self.username, password=self.password),
            cookie_domain=self._cookie_domain(),
        )
        _expect_ok(response.parsed, int(response.status_code), "login")
        self._logged_in = True
        return self.get_user_self()

    def ensure_session_initialized(self) -> None:
        if not self._logged_in:
            self.login()

    def get_user_self(self) -> DatabaseUser:
        self.ensure_session_initialized()
        response = get_api_v1_user_self.sync_detailed(client=self._api_client)
        parsed = _expect_ok(response.parsed, int(response.status_code), "get_user_self")
        if not isinstance(parsed, DatabaseUser):
            raise RuntimeError(f"get_user_self returned unexpected type: {type(parsed)!r}")
        return parsed

    def retrieve_default_bot(self) -> ContactsListedContact:
        self.ensure_session_initialized()
        response = get_api_v1_contacts_list.sync_detailed(client=self._api_client, page=1, limit=200)
        parsed = _expect_ok(response.parsed, int(response.status_code), "retrieve_default_bot")
        if not isinstance(parsed, ContactsPaginatedContacts):
            raise RuntimeError(f"contacts/list returned unexpected type: {type(parsed)!r}")

        rows = parsed.rows
        if _is_unset(rows):
            raise RuntimeError("contacts/list returned no rows")

        for row in rows:
            if not _is_unset(row.name) and row.name == "bot":
                return row
        raise RuntimeError("No default bot contact found")

    def create_interaction(
        self,
        tool_init: Optional[dict[str, Any]] = None,
        message: str = "",
    ) -> ChatsListedChat:
        self.ensure_session_initialized()
        default_bot = self.retrieve_default_bot()
        if _is_unset(default_bot.contact_token):
            raise RuntimeError("default bot is missing contact_token")

        shared_config = ChatsCreateChatSharedConfig.from_dict({**self.bot_config, "tool_init": tool_init or {}})
        body = ChatsCreateChat(
            contact_token=default_bot.contact_token,
            first_message=message,
            chat_type="interaction",
            shared_config=shared_config,
        )
        response = post_api_v1_chats_create.sync_detailed(client=self._api_client, body=body)
        parsed = _expect_ok(response.parsed, int(response.status_code), "create_interaction")
        if not isinstance(parsed, ChatsListedChat):
            raise RuntimeError(f"create_interaction returned unexpected type: {type(parsed)!r}")
        if not _is_unset(parsed.uuid):
            self._last_chat_uuid = parsed.uuid
        return parsed

    def list_interaction_messages(self, chat_uuid: str, page: int = 1, limit: int = 40) -> ChatsListedMessagesPage:
        self.ensure_session_initialized()
        response = get_api_v1_chats_chat_uuid_messages_list.sync_detailed(
            client=self._api_client,
            chat_uuid=chat_uuid,
            page=page,
            limit=limit,
        )
        parsed = _expect_ok(response.parsed, int(response.status_code), "list_interaction_messages")
        if not isinstance(parsed, ChatsListedMessagesPage):
            raise RuntimeError(f"list_interaction_messages returned unexpected type: {type(parsed)!r}")
        return parsed

    def interaction_wait_for_stop_signal(
        self,
        chat_uuid: Optional[str] = None,
        wait_seconds: int = 20,
        poll_interval: float = 0.5,
        quiet_seconds: float = 3.0,
    ) -> ChatsListedMessage | InteractionStopSignal:
        target_chat_uuid = chat_uuid or self._last_chat_uuid
        if not target_chat_uuid:
            raise ValueError("chat_uuid is required when no interaction has been created yet")

        deadline = time.time() + max(wait_seconds, 0)
        last_signature = ""
        last_change_at = time.time()
        latest_row: ChatsListedMessage | None = None

        while True:
            payload = self.list_interaction_messages(chat_uuid=target_chat_uuid, page=1, limit=100)
            rows = [] if _is_unset(payload.rows) else payload.rows

            signature_parts: list[str] = []
            for row in rows:
                latest_row = row
                row_uuid = "" if _is_unset(row.uuid) else row.uuid
                row_send_at = "" if _is_unset(row.send_at) else row.send_at
                row_text = "" if _is_unset(row.text) else row.text
                signature_parts.append(f"{row_uuid}|{row_send_at}|{row_text}")

                if not _is_unset(row.meta_data):
                    finished = row.meta_data.additional_properties.get("finished")
                    if finished is True:
                        return row

            signature = "\n".join(signature_parts)
            now = time.time()
            if signature != last_signature:
                last_signature = signature
                last_change_at = now
            elif now - last_change_at >= max(quiet_seconds, 0.5):
                latest_uuid = None
                if latest_row is not None and not _is_unset(latest_row.uuid):
                    latest_uuid = latest_row.uuid
                return InteractionStopSignal(
                    chat_uuid=target_chat_uuid,
                    reason=f"no message updates for {quiet_seconds:.1f}s",
                    latest_message_uuid=latest_uuid,
                )

            if time.time() >= deadline:
                raise TimeoutError(f"interaction did not emit a stop signal within {wait_seconds}s")
            time.sleep(max(poll_interval, 0.1))

    def get_interactions(self, page: int = 1, limit: int = 40, all_pages: bool = True) -> ChatsListedChatsPage:
        self.ensure_session_initialized()
        response = get_api_v1_chats_list.sync_detailed(
            client=self._api_client,
            page=page,
            limit=limit,
            chat_types="interaction",
        )
        parsed = _expect_ok(response.parsed, int(response.status_code), "get_interactions")
        if not isinstance(parsed, ChatsListedChatsPage):
            raise RuntimeError(f"get_interactions returned unexpected type: {type(parsed)!r}")

        if not all_pages or _is_unset(parsed.total_pages) or _is_unset(parsed.rows):
            return parsed

        total_pages = parsed.total_pages
        if total_pages <= page:
            return parsed

        merged_rows = list(parsed.rows)
        for next_page in range(page + 1, total_pages + 1):
            next_response = get_api_v1_chats_list.sync_detailed(
                client=self._api_client,
                page=next_page,
                limit=limit,
                chat_types="interaction",
            )
            next_parsed = _expect_ok(next_response.parsed, int(next_response.status_code), "get_interactions page")
            if not isinstance(next_parsed, ChatsListedChatsPage):
                raise RuntimeError(f"get_interactions page returned unexpected type: {type(next_parsed)!r}")
            if _is_unset(next_parsed.rows):
                continue
            merged_rows.extend(next_parsed.rows)

        return ChatsListedChatsPage(
            limit=parsed.limit,
            page=parsed.page,
            total_pages=parsed.total_pages,
            rows=merged_rows,
        )

    def get_interaction(self, chat_uuid: str) -> ChatsListedChat:
        self.ensure_session_initialized()
        response = get_api_v1_chats_chat_uuid.sync_detailed(client=self._api_client, chat_uuid=chat_uuid)
        parsed = _expect_ok(response.parsed, int(response.status_code), "get_interaction")
        if not isinstance(parsed, ChatsListedChat):
            raise RuntimeError(f"get_interaction returned unexpected type: {type(parsed)!r}")
        return parsed

    def get_interaction_confirmation_list(
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
                        if not isinstance(action, dict):
                            continue
                        action_id = str(action.get("action_id", "")).strip()
                        if not action_id:
                            continue
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
                        tool_input = confirmation_meta.get("tool_input")
                        if isinstance(tool_input, dict):
                            confirmation.tool_input = dict(tool_input)
                        tool_name = confirmation_meta.get("tool_name")
                        if isinstance(tool_name, str) and tool_name:
                            confirmation.source_tool_name = tool_name

                    args = tool_call.get("arguments")
                    if isinstance(args, dict):
                        confirmation.tool_call_arguments = dict(args)

                    suggested_inputs = None
                    if confirmation.tool_input and "suggested_inputs" in confirmation.tool_input:
                        suggested_inputs = confirmation.tool_input.get("suggested_inputs")
                    if suggested_inputs is None and confirmation.tool_call_arguments:
                        suggested_inputs = confirmation.tool_call_arguments.get("suggested_inputs")

                    if isinstance(suggested_inputs, str):
                        raw = suggested_inputs.strip()
                        if raw:
                            try:
                                confirmation.suggested_inputs = json.loads(raw)
                            except json.JSONDecodeError:
                                confirmation.suggested_inputs = raw
                    elif suggested_inputs is not None:
                        confirmation.suggested_inputs = suggested_inputs

                    action_by_id[action_id] = confirmation

            if action_by_id:
                return list(action_by_id.values())
            if has_finished_message or time.time() >= deadline:
                return []
            time.sleep(max(poll_interval, 0.1))

    def execute_confirm_action(
        self,
        chat_uuid: str,
        message_uuid: str,
        action_id: str,
        continue_after_execute: bool = True,
    ) -> dict[str, Any]:
        self.ensure_session_initialized()
        response = self._api_client.get_httpx_client().post(
            f"/api/v1/chats/{chat_uuid}/messages/{message_uuid}/confirm-actions/{action_id}/execute",
            json={"continue_after_execute": continue_after_execute},
        )
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise RuntimeError("execute_confirm_action returned non-object response")
        return payload

    def publish_chat(self, chat_uuid: str) -> ChatsSharedChatPublishResponse:
        self.ensure_session_initialized()
        response = post_api_chat_chat_uuid_publish.sync_detailed(client=self._api_client, chat_uuid=chat_uuid)
        parsed = _expect_ok(response.parsed, int(response.status_code), "publish_chat")
        if not isinstance(parsed, ChatsSharedChatPublishResponse):
            raise RuntimeError(f"publish_chat returned unexpected type: {type(parsed)!r}")
        return parsed

    def get_shared_interaction_url(self, chat_uuid: str) -> str:
        publish_data = self.publish_chat(chat_uuid)
        if _is_unset(publish_data.chat_share_uuid):
            raise RuntimeError("publish endpoint did not return chat_share_uuid")
        return f"{self.host}/interaction/{publish_data.chat_share_uuid}"

    def listen_shared_interaction_stream(
        self,
        chat_share_uuid: str,
        timeout_seconds: float = 30.0,
        max_events: Optional[int] = None,
    ) -> list[dict[str, Any]]:
        try:
            from websocket import create_connection  # type: ignore
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "websocket-client is required for websocket streaming. Install with: pip install websocket-client"
            ) from exc

        parsed_host = urlparse(self.host)
        if not parsed_host.netloc:
            raise ValueError(f"invalid host: {self.host}")
        ws_scheme = "wss" if parsed_host.scheme == "https" else "ws"
        ws_url = f"{ws_scheme}://{parsed_host.netloc}/ws/interaction/{chat_share_uuid}"

        headers: list[str] = []
        if self.api_token:
            headers.append(f"Authorization: Bearer {self.api_token}")

        cookie_pairs = []
        for cookie in self._api_client.get_httpx_client().cookies.jar:
            cookie_pairs.append(f"{cookie.name}={cookie.value}")
        if cookie_pairs:
            headers.append(f"Cookie: {'; '.join(cookie_pairs)}")

        events: list[dict[str, Any]] = []
        ws = create_connection(ws_url, timeout=timeout_seconds, header=headers)
        try:
            ws.settimeout(timeout_seconds)
            while True:
                if max_events is not None and max_events > 0 and len(events) >= max_events:
                    break
                raw_event = ws.recv()
                if not raw_event:
                    continue
                try:
                    parsed_event = json.loads(raw_event)
                except json.JSONDecodeError:
                    parsed_event = {"type": "raw", "raw": str(raw_event)}
                if isinstance(parsed_event, dict):
                    events.append(parsed_event)
                else:
                    events.append({"type": "raw", "raw": parsed_event})
        except Exception:
            pass
        finally:
            ws.close()

        return events


def main() -> None:
    parser = argparse.ArgumentParser(description="Open-Chat Python client")
    parser.add_argument("--host", default="http://localhost:1984")
    parser.add_argument("--username", default="admin")
    parser.add_argument("--password", default="password")
    parser.add_argument("--api-token", default="")
    parser.add_argument("--message", default="Hello from open_chat_client_python")
    args = parser.parse_args()

    client = OpenChatPythonClient(
        host=args.host,
        username=args.username,
        password=args.password,
        api_token=(args.api_token or None),
    )
    user = client.get_user_self() if args.api_token else client.login()
    print(f"Logged in as: {user.name if not _is_unset(user.name) else 'unknown'}")
    chat = client.create_interaction(message=args.message)
    print(f"Created interaction chat: {chat.uuid if not _is_unset(chat.uuid) else '<unknown>'}")


if __name__ == "__main__":
    main()
