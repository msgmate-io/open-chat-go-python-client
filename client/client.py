import argparse
import json
import time
from typing import Any, Optional
from urllib.parse import urlparse

import httpx
import requests

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
from .generated_api.models.user_user_login import UserUserLogin


DEFAULT_BOT_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 4096,
    "model": "qwen3-8b-instruct_vllm",
    "endpoint": "https://litellm.t1m.me/v1",
    "backend": "litellm",
    "context": 10,
    "system_prompt": "You are a helpful assistant.",
}


def _as_dict(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    to_dict = getattr(value, "to_dict", None)
    if callable(to_dict):
        parsed = to_dict()
        if isinstance(parsed, dict):
            return parsed
    raise RuntimeError(f"cannot convert value to dict: {type(value)!r}")


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
        self.session = requests.Session()
        self.bot_config = dict(DEFAULT_BOT_CONFIG)
        self._logged_in = api_token is not None
        self._last_chat_uuid: Optional[str] = None

        self._api_client = GeneratedClient(
            base_url=self.host,
            headers=self._headers(),
            timeout=httpx.Timeout(30.0),
            follow_redirects=True,
            raise_on_unexpected_status=False,
        )

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json", "Origin": self.host}
        if self.api_token:
            headers["Authorization"] = f"Bearer {self.api_token}"
        return headers

    def _sync_requests_to_httpx(self) -> None:
        httpx_client = self._api_client.get_httpx_client()
        httpx_client.cookies.clear()
        for name, value in self.session.cookies.get_dict().items():
            httpx_client.cookies.set(name, value)

    def _sync_httpx_to_requests(self) -> None:
        httpx_client = self._api_client.get_httpx_client()
        for cookie in httpx_client.cookies.jar:
            self.session.cookies.set(cookie.name, cookie.value, domain=cookie.domain, path=cookie.path)

    def _cookie_domain(self) -> str:
        parsed = urlparse(self.host)
        return parsed.hostname or ""

    def _raw_get(self, path: str, params: Optional[dict[str, Any]] = None) -> dict[str, Any]:
        response = self.session.get(f"{self.host}{path}", params=params, headers=self._headers(), timeout=30)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise RuntimeError(f"expected JSON object from {path}")
        return payload

    def setup_bot_config(self, bot_config: dict[str, Any]) -> None:
        self.bot_config = dict(bot_config)

    def login(self) -> dict[str, Any]:
        if self._logged_in:
            return self.get_user_self()

        self._sync_requests_to_httpx()
        response = post_api_v1_user_login.sync_detailed(
            client=self._api_client,
            body=UserUserLogin(email=self.username, password=self.password),
            cookie_domain=self._cookie_domain(),
        )
        self._sync_httpx_to_requests()
        if response.status_code >= 400:
            raise requests.RequestException(f"login failed: {response.status_code} {response.content!r}")

        self._logged_in = True
        return self.get_user_self()

    def ensure_session_initialized(self) -> None:
        if not self._logged_in:
            self.login()

    def get_user_self(self) -> dict[str, Any]:
        self.ensure_session_initialized()
        self._sync_requests_to_httpx()
        response = get_api_v1_user_self.sync_detailed(client=self._api_client)
        self._sync_httpx_to_requests()
        if response.status_code >= 400 or response.parsed is None or isinstance(response.parsed, str):
            raise requests.RequestException(f"get_user_self failed: {response.status_code} {response.content!r}")
        return _as_dict(response.parsed)

    def retrieve_default_bot(self) -> Optional[dict[str, Any]]:
        self.ensure_session_initialized()
        payload: dict[str, Any]
        try:
            self._sync_requests_to_httpx()
            response = get_api_v1_contacts_list.sync_detailed(client=self._api_client, page=1, limit=200)
            self._sync_httpx_to_requests()
            if response.status_code >= 400 or response.parsed is None or isinstance(response.parsed, str):
                raise requests.RequestException(f"contacts list failed: {response.status_code} {response.content!r}")
            payload = _as_dict(response.parsed)
        except Exception:
            payload = self._raw_get("/api/v1/contacts/list", params={"page": 1, "limit": 200})

        rows = payload.get("rows", [])
        if not isinstance(rows, list):
            return None
        for row in rows:
            if isinstance(row, dict) and row.get("name") == "bot":
                return row
        return None

    def create_interaction(self, tool_init: Optional[dict[str, Any]] = None, message: str = "") -> dict[str, Any]:
        self.ensure_session_initialized()
        default_bot = self.retrieve_default_bot()
        if not default_bot:
            raise RuntimeError("No default bot contact found")

        body = ChatsCreateChat(
            contact_token=str(default_bot["contact_token"]),
            first_message=message,
            chat_type="interaction",
            shared_config={**self.bot_config, "tool_init": tool_init or {}},
        )
        self._sync_requests_to_httpx()
        response = post_api_v1_chats_create.sync_detailed(client=self._api_client, body=body)
        self._sync_httpx_to_requests()
        if response.status_code >= 400 or response.parsed is None or isinstance(response.parsed, str):
            raise requests.RequestException(f"create_interaction failed: {response.status_code} {response.content!r}")

        created = _as_dict(response.parsed)
        chat_uuid = created.get("uuid")
        if isinstance(chat_uuid, str) and chat_uuid:
            self._last_chat_uuid = chat_uuid
        return created

    def interaction_wait_for_stop_signal(
        self,
        chat_uuid: Optional[str] = None,
        wait_seconds: int = 20,
        poll_interval: float = 0.5,
        quiet_seconds: float = 3.0,
    ) -> dict[str, Any]:
        target_chat_uuid = chat_uuid or self._last_chat_uuid
        if not target_chat_uuid:
            raise ValueError("chat_uuid is required when no interaction has been created yet")

        deadline = time.time() + max(wait_seconds, 0)
        last_signature = ""
        last_change_at = time.time()
        latest_row: dict[str, Any] = {}

        while True:
            payload = self.list_interaction_messages(chat_uuid=target_chat_uuid, page=1, limit=100)
            rows = payload.get("rows", []) if isinstance(payload, dict) else []

            signature_parts: list[str] = []
            for row in rows:
                if not isinstance(row, dict):
                    continue
                latest_row = row
                signature_parts.append(f"{row.get('uuid','')}|{row.get('send_at','')}|{row.get('text','')}")
                meta = row.get("meta_data")
                if isinstance(meta, dict) and meta.get("finished") is True:
                    return row

            signature = "\n".join(signature_parts)
            now = time.time()
            if signature != last_signature:
                last_signature = signature
                last_change_at = now
            elif now - last_change_at >= max(quiet_seconds, 0.5):
                return {
                    "chat_uuid": target_chat_uuid,
                    "signal": "inferred_stop",
                    "reason": f"no message updates for {quiet_seconds:.1f}s",
                    "latest_message_uuid": latest_row.get("uuid") if latest_row else None,
                }

            if time.time() >= deadline:
                raise TimeoutError(f"interaction did not emit a stop signal within {wait_seconds}s")
            time.sleep(max(poll_interval, 0.1))

    def list_interaction_messages(self, chat_uuid: str, page: int = 1, limit: int = 40) -> dict[str, Any]:
        self.ensure_session_initialized()
        self._sync_requests_to_httpx()
        response = get_api_v1_chats_chat_uuid_messages_list.sync_detailed(
            client=self._api_client,
            chat_uuid=chat_uuid,
            page=page,
            limit=limit,
        )
        self._sync_httpx_to_requests()
        if response.status_code >= 400 or response.parsed is None or isinstance(response.parsed, str):
            raise requests.RequestException(f"list_interaction_messages failed: {response.status_code} {response.content!r}")
        return _as_dict(response.parsed)

    def get_interactions(self, page: int = 1, limit: int = 40, all_pages: bool = True) -> dict[str, Any]:
        self.ensure_session_initialized()
        self._sync_requests_to_httpx()
        response = get_api_v1_chats_list.sync_detailed(
            client=self._api_client,
            page=page,
            limit=limit,
            chat_types="interaction",
        )
        self._sync_httpx_to_requests()
        if response.status_code >= 400 or response.parsed is None or isinstance(response.parsed, str):
            raise requests.RequestException(f"get_interactions failed: {response.status_code} {response.content!r}")

        payload = _as_dict(response.parsed)
        if not all_pages:
            return payload

        rows = payload.get("rows")
        total_pages = payload.get("total_pages")
        if not isinstance(rows, list) or not isinstance(total_pages, int) or total_pages <= page:
            return payload

        merged_rows = list(rows)
        for next_page in range(page + 1, total_pages + 1):
            self._sync_requests_to_httpx()
            next_response = get_api_v1_chats_list.sync_detailed(
                client=self._api_client,
                page=next_page,
                limit=limit,
                chat_types="interaction",
            )
            self._sync_httpx_to_requests()
            if next_response.status_code >= 400 or next_response.parsed is None or isinstance(next_response.parsed, str):
                break
            next_payload = _as_dict(next_response.parsed)
            next_rows = next_payload.get("rows")
            if isinstance(next_rows, list):
                merged_rows.extend(next_rows)

        payload["rows"] = merged_rows
        return payload

    def get_interaction(self, chat_uuid: str, include_share_info: bool = False) -> dict[str, Any]:
        self.ensure_session_initialized()
        self._sync_requests_to_httpx()
        response = get_api_v1_chats_chat_uuid.sync_detailed(client=self._api_client, chat_uuid=chat_uuid)
        self._sync_httpx_to_requests()
        if response.status_code >= 400 or response.parsed is None or isinstance(response.parsed, str):
            raise requests.RequestException(f"get_interaction failed: {response.status_code} {response.content!r}")

        payload = _as_dict(response.parsed)
        config = payload.get("config")
        interaction_details: dict[str, Any] = {}
        if isinstance(config, dict):
            for key in (
                "model",
                "backend",
                "max_tokens",
                "temperature",
                "context",
                "tools",
                "tool_init",
                "system_prompt",
            ):
                if key in config:
                    interaction_details[key] = config[key]
        payload["interaction_details"] = interaction_details
        return payload

    def get_interaction_confirmation_list(
        self,
        chat_uuid: str,
        wait_seconds: int = 10,
        poll_interval: float = 0.5,
    ) -> list[dict[str, Any]]:
        deadline = time.time() + max(wait_seconds, 0)
        confirmations: list[dict[str, Any]] = []

        while True:
            payload = self.list_interaction_messages(chat_uuid=chat_uuid, page=1, limit=100)
            rows = payload.get("rows", []) if isinstance(payload, dict) else []
            confirmations = []
            action_by_id: dict[str, dict[str, Any]] = {}
            has_finished_message = False

            for message in rows:
                meta = message.get("meta_data") if isinstance(message, dict) else None
                if not isinstance(meta, dict):
                    meta = {}
                if meta.get("finished") is True:
                    has_finished_message = True

                actions = meta.get("confirmable_actions")
                if isinstance(actions, list):
                    for action in actions:
                        if isinstance(action, dict):
                            action_id = str(action.get("action_id", "")).strip()
                            if action_id:
                                action_by_id[action_id] = dict(action)
                            else:
                                confirmations.append(dict(action))

                tool_calls = message.get("tool_calls") if isinstance(message, dict) else None
                if not isinstance(tool_calls, list):
                    continue

                for tool_call in tool_calls:
                    if not isinstance(tool_call, dict):
                        continue
                    action_id = str(tool_call.get("id", "")).strip()
                    if not action_id:
                        continue

                    merged = dict(action_by_id.get(action_id, {"action_id": action_id}))
                    confirmation_meta = tool_call.get("confirmation")
                    if isinstance(confirmation_meta, dict):
                        tool_input = confirmation_meta.get("tool_input")
                        if isinstance(tool_input, dict):
                            merged["tool_input"] = dict(tool_input)
                        tool_name = confirmation_meta.get("tool_name")
                        if isinstance(tool_name, str) and tool_name:
                            merged["source_tool_name"] = tool_name

                    args = tool_call.get("arguments")
                    if isinstance(args, dict):
                        merged["tool_call_arguments"] = dict(args)

                    suggested_inputs = None
                    tool_input = merged.get("tool_input")
                    if isinstance(tool_input, dict):
                        suggested_inputs = tool_input.get("suggested_inputs")
                    if suggested_inputs is None and isinstance(args, dict):
                        suggested_inputs = args.get("suggested_inputs")

                    if isinstance(suggested_inputs, str):
                        raw = suggested_inputs.strip()
                        if raw:
                            try:
                                merged["suggested_inputs"] = json.loads(raw)
                            except json.JSONDecodeError:
                                merged["suggested_inputs"] = raw
                    elif suggested_inputs is not None:
                        merged["suggested_inputs"] = suggested_inputs

                    action_by_id[action_id] = merged

            confirmations.extend(action_by_id.values())
            if confirmations:
                return confirmations
            if has_finished_message or time.time() >= deadline:
                return confirmations
            time.sleep(max(poll_interval, 0.1))

    def publish_chat(self, chat_uuid: str) -> dict[str, Any]:
        self.ensure_session_initialized()
        self._sync_requests_to_httpx()
        response = post_api_chat_chat_uuid_publish.sync_detailed(client=self._api_client, chat_uuid=chat_uuid)
        self._sync_httpx_to_requests()
        if response.status_code >= 400 or response.parsed is None or isinstance(response.parsed, str):
            raise requests.RequestException(f"publish_chat failed: {response.status_code} {response.content!r}")
        return _as_dict(response.parsed)

    def get_shared_interaction_url(self, chat_uuid: str) -> str:
        publish_data = self.publish_chat(chat_uuid)
        share_uuid = publish_data.get("chat_share_uuid")
        if not share_uuid:
            raise RuntimeError("publish endpoint did not return chat_share_uuid")
        return f"{self.host}/interaction/{share_uuid}"

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

        headers = []
        if self.api_token:
            headers.append(f"Authorization: Bearer {self.api_token}")
        else:
            self.ensure_session_initialized()

        cookie_dict = self.session.cookies.get_dict()
        if cookie_dict:
            headers.append(f"Cookie: {'; '.join(f'{k}={v}' for k, v in cookie_dict.items())}")

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
                events.append(parsed_event if isinstance(parsed_event, dict) else {"type": "raw", "raw": parsed_event})
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
    print(f"Logged in as: {user.get('name', 'unknown')}")
    chat = client.create_interaction(message=args.message)
    print(f"Created interaction chat: {chat.get('uuid', '<unknown>')}")


if __name__ == "__main__":
    main()
