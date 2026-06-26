# Open Chat Python Client Integration Guide (First-Class Bot Flow)

The client is now object-first and bot-centric.

Preferred flow:

1. Create `OpenChatClient`
2. Use `interact(...)` for the shortest path, or resolve a bot with `get_bot(...)`
3. Create an interaction
4. Work with the returned `InteractionSession`

## Quickstart

```python
from client import OpenChatClient, PasswordAuth, ToolName

client = OpenChatClient(
    base_url="http://localhost:1984",
    auth=PasswordAuth(email="admin", password="password"),
)

client.login()

# shortest path
interaction = client.interact(message="Draft a concise support response")

# explicit bot handle path
bot = client.get_bot("little_world_chat")
interaction = bot.create_interaction(message="Draft a concise support response")

final = interaction.wait_until_finished(timeout_seconds=30)
print(type(final).__name__)
```

## Main API surface

- `OpenChatClient.list_bots() -> list[Bot]`
- `OpenChatClient.get_bots() -> list[Bot]`
- `OpenChatClient.get_default_bot() -> Bot`
- `OpenChatClient.get_bot(identifier: str) -> Bot`
- `OpenChatClient.interact(message, bot="bot", tool_init=None, overrides=None) -> InteractionSession`
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

## Generated tool payload types (call + init)

Per-tool classes are auto-generated from OpenAPI under `client/generated_api/models/`.

Examples include:

- `get_weather_call.GetWeatherCall`
- `little_world_chat_reply_call.LittleWorldChatReplyCall`
- `little_world_chat_reply_init.LittleWorldChatReplyInit`

Use typed init payloads directly in interaction creation:

```python
from client import OpenChatClient, PasswordAuth
from client.generated_api.models.little_world_chat_reply_init import LittleWorldChatReplyInit

client = OpenChatClient(base_url="http://localhost:1984", auth=PasswordAuth("admin", "password"))
client.login()

interaction = client.get_bot("bot").create_interaction(
    message="Please answer as support agent",
    overrides={"tools": [ToolName.LITTLE_WORLD_CHAT_REPLY]},
    tool_init={
        ToolName.LITTLE_WORLD_CHAT_REPLY: LittleWorldChatReplyInit(
            api_host="https://app.littleworld.com",
            chat_uuid="chat-uuid",
            csrf_token="csrf",
            session_id="session",
        )
    },
)
```

Use typed call payload models with generated validate endpoints:

```python
from client.generated_api.api.tools.post_api_v1_tools_typing_little_world_chat_reply_call_validate import sync as validate_call
from client.generated_api.models.little_world_chat_reply_call import LittleWorldChatReplyCall

payload = LittleWorldChatReplyCall(message="Hello from support")
validate_call(client=client._api, body=payload)
```

Runtime tool names (fetched from server, no hardcoded list required):

```python
tool_names = client.list_tool_names()
ToolNameDynamic = client.get_tool_name_enum()

print(tool_names)
print(ToolNameDynamic.LITTLE_WORLD_CHAT_REPLY)
```

## Notes

- Bot discovery uses existing automated contacts (`is_automated`) and profile data.
- Bot default runtime config is derived from bot profile models when available, with fallback defaults.
- Old dict-style integration is deprecated; use object attributes and methods.
