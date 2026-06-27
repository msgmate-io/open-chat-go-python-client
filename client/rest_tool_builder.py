import json
from typing import Any


class RESTToolBindingBuilder:
    def __init__(self, parent: "RESTToolBuilder", input_name: str, source: str):
        self._parent = parent
        self._input_name = input_name.strip()
        self._source = source
        if not self._input_name:
            raise ValueError("input_name is required")

    def _add(self, where: str, name: str) -> "RESTToolBuilder":
        param_name = name.strip()
        if not param_name:
            raise ValueError("binding target name is required")
        self._parent._param_bindings.append(
            {
                "input_name": self._input_name,
                "source": self._source,
                "in": where,
                "name": param_name,
            }
        )
        return self._parent

    def to_path(self, name: str) -> "RESTToolBuilder":
        return self._add("path", name)

    def to_query(self, name: str) -> "RESTToolBuilder":
        return self._add("query", name)

    def to_header(self, name: str) -> "RESTToolBuilder":
        return self._add("header", name)

    def to_body(self, name: str) -> "RESTToolBuilder":
        return self._add("body", name)


class RESTToolBuilder:
    def __init__(self, name: str, description: str = ""):
        self._name = name.strip()
        if not self._name:
            raise ValueError("name is required")
        self._description = description

        self._openapi_source_type = ""
        self._openapi_source = ""
        self._operation_id = ""
        self._http_method = ""
        self._path = ""
        self._base_url_source = ""
        self._base_url_input_name = ""
        self._param_bindings: list[dict[str, Any]] = []
        self._safety_policy: dict[str, Any] = {}
        self._enabled = True

    def description(self, value: str) -> "RESTToolBuilder":
        self._description = value
        return self

    def openapi_inline(self, document: dict[str, Any] | str) -> "RESTToolBuilder":
        if isinstance(document, str):
            src = document.strip()
            if not src:
                raise ValueError("openapi document is required")
            self._openapi_source = src
        else:
            self._openapi_source = json.dumps(document)
        self._openapi_source_type = "inline"
        return self

    def openapi_url(self, url: str) -> "RESTToolBuilder":
        source = url.strip()
        if not source:
            raise ValueError("openapi url is required")
        self._openapi_source_type = "url"
        self._openapi_source = source
        return self

    def operation(self, operation_id: str) -> "RESTToolBuilder":
        value = operation_id.strip()
        if not value:
            raise ValueError("operation_id is required")
        self._operation_id = value
        return self

    def route(self, method: str, path: str) -> "RESTToolBuilder":
        method_value = method.strip().lower()
        path_value = path.strip()
        if not method_value:
            raise ValueError("method is required")
        if not path_value:
            raise ValueError("path is required")
        self._http_method = method_value
        self._path = path_value
        return self

    def base_url_from_init(self, input_name: str = "api_host") -> "RESTToolBuilder":
        field = input_name.strip()
        if not field:
            raise ValueError("input_name is required")
        self._base_url_source = "init"
        self._base_url_input_name = field
        return self

    def base_url_from_call(self, input_name: str = "api_host") -> "RESTToolBuilder":
        field = input_name.strip()
        if not field:
            raise ValueError("input_name is required")
        self._base_url_source = "call"
        self._base_url_input_name = field
        return self

    def bind_init(self, input_name: str) -> RESTToolBindingBuilder:
        return RESTToolBindingBuilder(parent=self, input_name=input_name, source="init")

    def bind_call(self, input_name: str) -> RESTToolBindingBuilder:
        return RESTToolBindingBuilder(parent=self, input_name=input_name, source="call")

    def allow_hosts(self, *hosts: str) -> "RESTToolBuilder":
        values = [host.strip().lower() for host in hosts if host.strip()]
        self._safety_policy["allow_hosts"] = values
        return self

    def allow_private_ips(self, enabled: bool = True) -> "RESTToolBuilder":
        self._safety_policy["allow_private_ips"] = bool(enabled)
        return self

    def timeout_seconds(self, seconds: int) -> "RESTToolBuilder":
        self._safety_policy["timeout_seconds"] = int(seconds)
        return self

    def max_response_body_bytes(self, limit: int) -> "RESTToolBuilder":
        self._safety_policy["max_response_body_bytes"] = int(limit)
        return self

    def enabled(self, value: bool = True) -> "RESTToolBuilder":
        self._enabled = bool(value)
        return self

    def enable(self) -> "RESTToolBuilder":
        return self.enabled(True)

    def disable(self) -> "RESTToolBuilder":
        return self.enabled(False)

    def build(self) -> dict[str, Any]:
        if not self._openapi_source_type:
            raise ValueError("openapi source is required, call openapi_inline(...) or openapi_url(...)")
        if not self._openapi_source:
            raise ValueError("openapi source content is required")
        if not self._operation_id and (not self._http_method or not self._path):
            raise ValueError("operation_id or route(method, path) is required")

        result: dict[str, Any] = {
            "name": self._name,
            "description": self._description,
            "openapi_source_type": self._openapi_source_type,
            "openapi_source": self._openapi_source,
            "param_bindings": list(self._param_bindings),
            "safety_policy": dict(self._safety_policy),
            "enabled": self._enabled,
        }
        if self._operation_id:
            result["operation_id"] = self._operation_id
        if self._http_method:
            result["http_method"] = self._http_method
        if self._path:
            result["path"] = self._path
        if self._base_url_source:
            result["base_url_source"] = self._base_url_source
        if self._base_url_input_name:
            result["base_url_input_name"] = self._base_url_input_name
        return result
