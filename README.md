### Open Chat Python Client

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
