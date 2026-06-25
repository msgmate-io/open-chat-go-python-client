# Open Chat Python Client Integration Guide

This guide is for another agent (or engineer) integrating the improved Open Chat Python client into a separate project.

The client now has two layers:

- `generated_api/`: typed endpoint client generated from backend API docs
- `OpenChatPythonClient`: ergonomic high-level wrapper for common interaction flows

Use `OpenChatPythonClient` unless you explicitly need low-level generated endpoint calls.

Important: this client is now breaking-change typed-first. Legacy dict-style payload usage is removed.

## 1) Install

Choose one:

### A. From GitHub (recommended for external projects)

```bash
pip install "open_chat_client_python @ git+https://github.com/msgmate-io/open-chat-go-python-client.git"
```

Or pin a tag:

```bash
pip install "open_chat_client_python @ git+https://github.com/msgmate-io/open-chat-go-python-client.git@<tag>"
```

### B. Editable install from monorepo

```bash
pip install -e ./clients/oc_python_client
```

## 2) Basic usage

```python
from client.client import OpenChatPythonClient

client = OpenChatPythonClient(
    host="http://localhost:1984",
    username="admin",
    password="password",
)

user = client.login()
print(user.name)

chat = client.create_interaction(message="Hello from integration")
chat_uuid = chat.uuid

messages = client.list_interaction_messages(chat_uuid, page=1, limit=40)
print(len(messages.rows))
```

## 3) Auth modes

### Username/password (session cookie)

- Provide `username` + `password`
- Call `login()` once
- Cookie/session automatically reused by wrapper

### API token

```python
client = OpenChatPythonClient(host="http://localhost:1984", api_token="ocat_xxx")
user = client.get_user_self()
```

- For token auth, no explicit `login()` needed

## 4) Recommended integration pattern

For worker jobs / task queues:

1. Create one `OpenChatPythonClient` per task execution
2. Set deterministic bot config with `setup_bot_config(...)`
3. Create interaction with optional `tool_init`
4. Poll with `interaction_wait_for_stop_signal(...)` or inspect messages directly
5. Optionally publish interaction and persist URL

Example:

```python
client.setup_bot_config(
    {
        "temperature": 0.0,
        "max_tokens": 8000,
        "tools": ["little_world__chat_reply"],
        "model": "qwen3-8b-instruct_vllm",
        "endpoint": "https://litellm.t1m.me/v1",
        "backend": "litellm",
        "context": 8000,
        "system_prompt": "You are a helpful assistant.",
    }
)

chat = client.create_interaction(
    message="Reply to the latest user message.",
    tool_init={
        "little_world__chat_reply": {
            "session_id": "...",
            "csrf_token": "...",
            "api_host": "http://host.docker.internal:1984",
            "chat_uuid": "...",
        }
    },
)

finished = client.interaction_wait_for_stop_signal(chat_uuid=chat.uuid, wait_seconds=30)
```

## 5) Key wrapper methods you should use

- `login()`
- `get_user_self()`
- `setup_bot_config(bot_config)`
- `create_interaction(message=..., tool_init=...)`
- `list_interaction_messages(chat_uuid, page=1, limit=40)`
- `get_interactions(page=1, limit=40, all_pages=True)`
- `get_interaction(chat_uuid)`
- `get_interaction_confirmation_list(chat_uuid)`
- `publish_chat(chat_uuid)`
- `get_shared_interaction_url(chat_uuid)`

## 6) Migrating from old/untyped usage

If your existing code manually calls many raw endpoints:

- Replace direct login/self/chats/messages HTTP calls with wrapper methods above.
- Keep your workflow logic (task orchestration, DB writes, permission checks) unchanged.
- Keep your existing `tool_init` payload structure; wrapper passes it through in `shared_config.tool_init`.

If your old code depended on raw `dict` payloads, migrate to typed attributes (for example `message.sender_id`, `page.rows`, `chat.uuid`).

## 7) When to use generated typed endpoints directly

Only if you need endpoint coverage not wrapped yet.

Example:

```python
from client.generated_api import Client
from client.generated_api.api.tools import get_api_v1_tools_list

api = Client(base_url="http://localhost:1984")
result = get_api_v1_tools_list.sync_detailed(client=api)
```

Note: for normal integrations, prefer `OpenChatPythonClient`.

## 8) Regenerating typed base client (for backend API changes)

From monorepo root:

```bash
python3 development/scripts/update_oc_python_client_base.py
```

What it does:

1. Reads Swagger 2.0 schema from `backend/server/swagger.json`
2. Converts to OpenAPI 3 via `swagger2openapi`
3. Generates typed client with `openapi-python-client`
4. Writes output to `clients/oc_python_client/client/generated_api/`

Generator config is in:

- `clients/oc_python_client/openapi-python-client-config.yaml`

## 9) Validation checklist in the consuming project

Run these after integration:

1. `login()` succeeds and returns user data
2. `create_interaction()` returns a chat UUID
3. `list_interaction_messages()` returns rows without parsing issues
4. Tool-call flow works with your `tool_init`
5. `get_shared_interaction_url()` returns a valid URL

If you have tests, include at least one mocked and one real backend run.

## 10) Troubleshooting

### `No default bot contact found`

- Ensure the authenticated user has the bot contact available in `/api/v1/contacts/list`.

### Auth/session issues in containers

- Confirm backend URL and cookie domain behavior (`host.docker.internal` is often required from containerized workers).

### Generated model parse mismatch

- Fix Swagger annotations in backend and regenerate.

### Tool calls do not happen

- Check `system_prompt`, `tools`, and `tool_init` keys.
- Verify tool names exactly match backend registered tool names.

## 11) Minimal agent handoff prompt

Use this prompt for another coding agent in your other project:

"Integrate `open_chat_client_python` using `OpenChatPythonClient` (not raw requests). Replace manual login/chats/messages/publish calls with wrapper methods. Keep existing orchestration logic and tool_init payloads. Add a smoke test that logs in, creates an interaction, waits for stop signal, and verifies messages are returned."
