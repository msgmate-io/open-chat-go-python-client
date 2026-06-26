# Open Chat Python Client Integration Guide (First-Class Bot Flow)

The client is now object-first and bot-centric.

Preferred flow:

1. Create `OpenChatClient`
2. Resolve a bot with `get_bot(...)`
3. Create an interaction from the bot handle
4. Work with the returned `InteractionSession`

## Quickstart

```python
from client import OpenChatClient, PasswordAuth

client = OpenChatClient(
    base_url="http://localhost:1984",
    auth=PasswordAuth(email="admin", password="password"),
)

client.login()

bot = client.get_bot("little_world_chat")
interaction = bot.create_interaction(
    message="Draft a concise support response",
    tool_init={"little_world__chat_reply": {"session_id": "..."}},
)

final = interaction.wait_until_finished(timeout_seconds=30)
print(type(final).__name__)
```

## Main API surface

- `OpenChatClient.list_bots() -> list[Bot]`
- `OpenChatClient.get_bot(identifier: str) -> Bot`
- `Bot.create_interaction(message, tool_init=None, overrides=None) -> InteractionSession`
- `InteractionSession.messages(page=1, limit=40) -> MessagesPage`
- `InteractionSession.wait_until_finished(...) -> Message | InteractionStopSignal`
- `InteractionSession.publish() -> ChatsSharedChatPublishResponse`
- `InteractionSession.shared_url() -> str`

## Authentication

Password auth:

```python
from client import OpenChatClient, PasswordAuth
client = OpenChatClient(base_url="http://localhost:1984", auth=PasswordAuth("admin", "password"))
client.login()
```

Token auth:

```python
from client import OpenChatClient, TokenAuth
client = OpenChatClient(base_url="http://localhost:1984", auth=TokenAuth("ocat_xxx"))
me = client.me()
```

## Regenerate typed base client

```bash
python3 development/scripts/update_oc_python_client_base.py
```

## Notes

- Bot discovery uses existing automated contacts (`is_automated`) and profile data.
- Bot default runtime config is derived from bot profile models when available, with fallback defaults.
- Old dict-style integration is deprecated; use object attributes and methods.
