### Open Chat Python Client

Install directly from GitHub:

```bash
pip install git+https://github.com/msgmate-io/open-chat-go-python-client.git
```

Install locally (from this monorepo root):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ./clients/oc_python_client
```

Run the CLI:

```bash
oc_client --host http://localhost:1984 --username admin --password password --message "hi"
```

Use the integration test script in this repository:

```bash
python development/scripts/test_client.py
```
