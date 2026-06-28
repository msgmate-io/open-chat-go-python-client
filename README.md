### Open Chat Python Client

This package now has two layers:

- Typed base client generated from backend API docs (`backend/server/swagger.json`) via `openapi-python-client`
- Handwritten `OpenChatClient` wrapper in `client/client.py` for higher-level workflows

Breaking change: the wrapper is now typed-first and returns model objects (not dict payloads).

Comprehensive integration guide for external projects:

- `clients/oc_python_client/INTEGRATION_GUIDE.md`

Install directly from GitHub:

```bash
pip install git+https://github.com/msgmate-io/open-chat-go-python-client.git
```

For `requirements.txt`, add this exact line:

```txt
open_chat_client_python @ git+https://github.com/msgmate-io/open-chat-go-python-client.git
```

For a pinned release tag in `requirements.txt`:

```txt
open_chat_client_python @ git+https://github.com/msgmate-io/open-chat-go-python-client.git@open-chat-pr-alpha-release-0.0.264-2d1aef2d7085
```

Install locally (from this monorepo root):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ./clients/oc_python_client
```

Run the CLI:

```bash
open_chat_client_python --host http://localhost:1984 --username admin --password password --message "hi"

# or authenticate with an API token
open_chat_client_python --host http://localhost:1984 --api-token ocat_xxx --message "hi"

# legacy alias (still supported)
oc_client --host http://localhost:1984 --api-token ocat_xxx --message "hi"
```

Use the integration test script in this repository:

```bash
python development/scripts/test_client.py
```

Python API example:

```python
from client.client import OpenChatClient, PasswordAuth
from client import ToolName

client = OpenChatClient(
    base_url="http://localhost:1984",
    auth=PasswordAuth(email="admin", password="password"),
)
client.login()

# Simplest flow: use default bot + one call
interaction = client.interact(message="Hello from Python")
print("Chat UUID:", interaction.uuid)

final = interaction.wait_until_finished(timeout_seconds=20)
print("Finished payload type:", type(final).__name__)
```

Recommended clean usage options:

- `client.interact("...")` for fastest path
- `client.get_default_bot().create_interaction(...)` when explicit bot handle helps
- `client.get_bot("support_agent").create_interaction(...)` when selecting named bots

Regenerate the typed base client:

```bash
python3 development/scripts/update_oc_python_client_base.py
```

The generator script converts Swagger 2.0 to OpenAPI 3.0 with `swagger2openapi`, then runs `openapi-python-client` and updates `clients/oc_python_client/client/generated_api/`.

Tool call/init payload types are now generated automatically as model classes.

Example (typed call validation):

```python
from client.client import OpenChatClient, PasswordAuth
from client.generated_api.api.tools.post_api_v1_tools_typing_get_weather_call_validate import sync as validate_weather_call
from client.generated_api.models.get_weather_call import GetWeatherCall

client = OpenChatClient(base_url="http://localhost:1984", auth=PasswordAuth("admin", "password"))
client.login()

interaction = client.get_bot("bot").create_interaction(
    message="Should I carry an umbrella in Berlin today?",
    overrides={"tools": [ToolName.GET_WEATHER]},
)

# Typed call payload class from generated OpenAPI models
typed_call = GetWeatherCall(location="Berlin")
validate_weather_call(client=client._api, body=typed_call)
```

If you want tool names fetched from the server at runtime (no hardcoded list), use:

```python
runtime_tools = client.list_tool_names()
ToolNameDynamic = client.get_tool_name_enum()

print(runtime_tools)
print(ToolNameDynamic.GET_WEATHER)
```
