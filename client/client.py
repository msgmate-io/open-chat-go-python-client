import argparse
import json
import time
from typing import Any, Dict, Optional

import requests


DEFAULT_BOT_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 4096,
    "model": "deepseek-ai/DeepSeek-V4-Flash",
    "endpoint": "https://api.deepinfra.com/v1/openai",
    "backend": "deepinfra",
    "context": 10,
    "system_prompt": "You are a helpful assistant.",
}


class OpenChatPythonClient:
    def __init__(self, host: str = "http://localhost:1984", username: str = "admin", password: str = "password", api_token: Optional[str] = None):
        self.host = host.rstrip("/")
        self.username = username
        self.password = password
        self.api_token = api_token
        self.session = requests.Session()
        self.bot_config = dict(DEFAULT_BOT_CONFIG)
        self._logged_in = api_token is not None

    def _headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json", "Origin": self.host}
        if self.api_token:
            headers["Authorization"] = f"Bearer {self.api_token}"
        return headers

    def setup_bot_config(self, bot_config: Dict[str, Any]) -> None:
        self.bot_config = dict(bot_config)

    def login(self) -> Dict[str, Any]:
        if self._logged_in:
            return self.get_user_self()

        cookie_domain = self.host.replace("http://", "").replace("https://", "").split(":")[0]
        login_url = f"{self.host}/api/v1/user/login?cookie_domain={cookie_domain}"
        response = self.session.post(
            login_url,
            json={"email": self.username, "password": self.password},
            headers=self._headers(),
            timeout=20,
        )
        response.raise_for_status()

        payload = response.json() if response.content else {}
        self._logged_in = True
        if isinstance(payload, dict) and payload.get("user"):
            return payload["user"]
        return self.get_user_self()

    def ensure_session_initialized(self) -> None:
        if not self._logged_in:
            self.login()

    def get_user_self(self) -> Dict[str, Any]:
        response = self.session.get(
            f"{self.host}/api/v1/user/self",
            headers=self._headers(),
            timeout=20,
        )
        response.raise_for_status()
        return response.json()

    def retrieve_default_bot(self) -> Optional[Dict[str, Any]]:
        self.ensure_session_initialized()
        response = self.session.get(
            f"{self.host}/api/v1/contacts/list",
            headers=self._headers(),
            timeout=20,
        )
        response.raise_for_status()
        rows = response.json().get("rows", [])
        for row in rows:
            if row.get("name") == "bot":
                return row
        return None

    def create_interaction(self, tool_init: Optional[Dict[str, Any]] = None, message: str = "") -> Dict[str, Any]:
        self.ensure_session_initialized()
        default_bot = self.retrieve_default_bot()
        if not default_bot:
            raise RuntimeError("No default bot contact found")

        payload = {
            "contact_token": default_bot["contact_token"],
            "first_message": message,
            "chat_type": "interaction",
            "shared_config": {
                **self.bot_config,
                "tool_init": tool_init or {},
            },
        }

        response = self.session.post(
            f"{self.host}/api/v1/chats/create",
            json=payload,
            headers=self._headers(),
            timeout=30,
        )
        response.raise_for_status()
        return response.json()

    def list_interaction_messages(self, chat_uuid: str, page: int = 1, limit: int = 40) -> Dict[str, Any]:
        self.ensure_session_initialized()
        response = self.session.get(
            f"{self.host}/api/v1/chats/{chat_uuid}/messages/list",
            params={"page": page, "limit": limit},
            headers=self._headers(),
            timeout=20,
        )
        response.raise_for_status()
        return response.json()

    def get_interaction_confirmation_list(self, chat_uuid: str, wait_seconds: int = 0, poll_interval: float = 0.5) -> list[Dict[str, Any]]:
        deadline = time.time() + max(wait_seconds, 0)
        confirmations: list[Dict[str, Any]] = []

        while True:
            payload = self.list_interaction_messages(chat_uuid=chat_uuid, page=1, limit=100)
            rows = payload.get("rows", []) if isinstance(payload, dict) else []
            confirmations = []
            action_by_id: Dict[str, Dict[str, Any]] = {}
            for message in rows:
                meta = message.get("meta_data") if isinstance(message, dict) else None
                if not isinstance(meta, dict):
                    meta = {}

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

                    base = action_by_id.get(action_id, {"action_id": action_id})
                    merged = dict(base)

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

            if confirmations or time.time() >= deadline:
                return confirmations
            time.sleep(max(poll_interval, 0.1))

    def publish_chat(self, chat_uuid: str) -> Dict[str, Any]:
        self.ensure_session_initialized()
        response = self.session.post(
            f"{self.host}/api/chat/{chat_uuid}/publish",
            headers=self._headers(),
            timeout=20,
        )
        response.raise_for_status()
        return response.json()

    def get_shared_interaction_url(self, chat_uuid: str) -> str:
        publish_data = self.publish_chat(chat_uuid)
        share_uuid = publish_data.get("chat_share_uuid")
        if not share_uuid:
            raise RuntimeError("publish endpoint did not return chat_share_uuid")
        return f"{self.host}/interaction/{share_uuid}"


def main() -> None:
    parser = argparse.ArgumentParser(description="MVP Open-Chat Python client")
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
