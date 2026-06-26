# Open Chat Python Client Integration Guide

This client is bot-first and typed-first.

Typical flow:

1. Create `OpenChatClient` and authenticate.
2. Create or select a bot.
3. Create an interaction on that bot.
4. Poll messages / wait for completion.

## Quickstart

```python
from client import OpenChatClient, PasswordAuth

client = OpenChatClient(
    base_url="http://localhost:1984",
    auth=PasswordAuth(email="admin", password="password"),
)
client.login()

interaction = client.interact(message="Draft a concise support response")
final = interaction.wait_until_finished(timeout_seconds=30)
print(type(final).__name__)
```

## Create Bots

Use `create_bot(...)` to create a user-owned bot with default interaction config.

```python
bot = client.create_bot(
    name="support_agent",
    description="Customer support helper",
    default_shared_config={
        "model": "qwen3-8b-instruct_vllm",
        "backend": "litellm",
        "endpoint": "https://litellm.t1m.me/v1",
        "temperature": 0.2,
        "max_tokens": 2048,
        "system_prompt": "You are a concise support assistant.",
    },
)
print(bot.uuid, bot.name)
```

## List Owned Bots

```python
owned_bots = client.list_owned_bots()
for b in owned_bots:
    print(b.uuid, b.name)
```

If you also want visible public bots:

```python
visible_bots = client.list_bots(include_public=True)
```

## Use Specific Bots for Interactions

You can resolve by bot UUID or owner-scoped name.

```python
bot = client.get_bot("support_agent")
# or: bot = client.get_bot("<bot-uuid>")

interaction = bot.create_interaction(
    message="Customer asks for a refund policy summary.",
)

print(interaction.uuid)
```

Shortcut form:

```python
interaction = client.interact(
    bot="support_agent",
    message="Answer as a support specialist",
)
```

## Typed Tool Usage In Interactions

Tool names:

- Static generated enum: `ToolName`
- Runtime-fetched enum: `client.get_tool_name_enum()`

```python
from client import ToolName
from client.generated_api.models.little_world_chat_reply_init import LittleWorldChatReplyInit

interaction = client.get_bot("support_agent").create_interaction(
    message="Reply politely",
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

Runtime enum example:

```python
ToolNameDynamic = client.get_tool_name_enum()
print(ToolNameDynamic.GET_CURRENT_TIME)
print(client.list_tool_names())
```

## Generated Tool Payload Models

Per-tool payload classes are auto-generated under `client/generated_api/models/`,
for example:

- `get_weather_call.GetWeatherCall`
- `little_world_chat_reply_call.LittleWorldChatReplyCall`
- `little_world_chat_reply_init.LittleWorldChatReplyInit`

You can validate typed call payloads via generated endpoints:

```python
from client.generated_api.api.tools.post_api_v1_tools_typing_little_world_chat_reply_call_validate import sync as validate_call
from client.generated_api.models.little_world_chat_reply_call import LittleWorldChatReplyCall

payload = LittleWorldChatReplyCall(message="Hello from support")
validate_call(client=client._api, body=payload)
```

## Core API Surface

- `OpenChatClient.create_bot(...) -> Bot`
- `OpenChatClient.update_bot(identifier, ...) -> Bot`
- `OpenChatClient.delete_bot(identifier) -> Bot`
- `OpenChatClient.list_owned_bots() -> list[Bot]`
- `OpenChatClient.list_bots(include_public=False) -> list[Bot]`
- `OpenChatClient.get_bot(identifier) -> Bot`
- `OpenChatClient.interact(message, bot="bot", tool_init=None, overrides=None) -> InteractionSession`
- `Bot.create_interaction(message, tool_init=None, overrides=None) -> InteractionSession`
- `InteractionSession.messages(page=1, limit=40) -> MessagesPage`
- `InteractionSession.wait_until_finished(...) -> Message | InteractionStopSignal`
- `InteractionSession.publish() -> ChatsSharedChatPublishResponse`
- `InteractionSession.shared_url() -> str`

## Regenerate Typed Client

```bash
python3 development/scripts/update_oc_python_client_base.py
```
