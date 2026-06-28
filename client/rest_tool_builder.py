import json
import copy
from typing import Any


def _extract_ref_schema_name(ref: str) -> str | None:
    prefix = "#/components/schemas/"
    if ref.startswith(prefix):
        return ref[len(prefix) :]
    return None


def _collect_schema_refs(value: Any, refs: set[str]) -> None:
    if isinstance(value, dict):
        ref_name = _extract_ref_schema_name(str(value.get("$ref", "")))
        if ref_name:
            refs.add(ref_name)
        for nested in value.values():
            _collect_schema_refs(nested, refs)
    elif isinstance(value, list):
        for item in value:
            _collect_schema_refs(item, refs)


def _collect_component_schemas(document: dict[str, Any], schema_names: tuple[str, ...]) -> dict[str, Any]:
    all_schemas = document.get("components", {}).get("schemas", {})
    if not isinstance(all_schemas, dict):
        return {}

    collected: dict[str, Any] = {}
    pending = list(dict.fromkeys(schema_names))
    seen: set[str] = set()

    while pending:
        name = pending.pop()
        if name in seen or name not in all_schemas:
            continue
        seen.add(name)
        component = copy.deepcopy(all_schemas[name])
        collected[name] = component

        nested_refs: set[str] = set()
        _collect_schema_refs(component, nested_refs)
        pending.extend(sorted(nested_refs - seen))

    if not collected:
        return {}
    return {"schemas": collected}


def reduce_openapi_to_endpoint(
    document: dict[str, Any] | str,
    *,
    path: str,
    method: str,
    info_title: str | None = None,
    info_version: str = "1.0.0",
    extra_parameters: list[dict[str, Any]] | None = None,
    request_body: dict[str, Any] | None = None,
    component_schema_names: tuple[str, ...] = (),
    keep_responses: bool = False,
    servers: list[dict[str, Any]] | None = None,
) -> tuple[str, dict[str, Any]]:
    source = json.loads(document) if isinstance(document, str) else copy.deepcopy(document)
    selected_path = path.strip()
    selected_method = method.strip().lower()

    if not selected_path:
        raise ValueError("path is required")
    if not selected_method:
        raise ValueError("method is required")

    path_item = source.get("paths", {}).get(selected_path)
    if not isinstance(path_item, dict):
        raise RuntimeError(f"OpenAPI path not found: {selected_path}")

    operation = copy.deepcopy(path_item.get(selected_method, {}))
    if not isinstance(operation, dict):
        operation = {}
    operation_id = str(operation.get("operationId", "")).strip()
    if not operation_id:
        raise RuntimeError(f"OpenAPI operation missing operationId: {selected_path} {selected_method}")

    merged_params: list[Any] = []
    if isinstance(path_item.get("parameters"), list):
        merged_params.extend(copy.deepcopy(path_item["parameters"]))
    if isinstance(operation.get("parameters"), list):
        merged_params.extend(copy.deepcopy(operation["parameters"]))
    if extra_parameters:
        merged_params.extend(copy.deepcopy(extra_parameters))
    operation["parameters"] = merged_params

    if request_body is not None:
        operation["requestBody"] = copy.deepcopy(request_body)
    if not keep_responses:
        operation.pop("responses", None)

    referenced_schema_names: set[str] = set(component_schema_names)
    _collect_schema_refs(operation, referenced_schema_names)
    components = _collect_component_schemas(source, tuple(sorted(referenced_schema_names)))

    reduced_doc: dict[str, Any] = {
        "openapi": source.get("openapi", "3.0.3"),
        "info": {
            "title": (info_title.strip() if isinstance(info_title, str) and info_title.strip() else "API"),
            "version": info_version,
        },
        "paths": {selected_path: {selected_method: operation}},
        "components": components,
    }
    if servers is not None:
        reduced_doc["servers"] = copy.deepcopy(servers)
    return operation_id, reduced_doc


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

    def openapi_endpoint(
        self,
        document: dict[str, Any] | str,
        *,
        path: str,
        method: str,
        info_title: str | None = None,
        info_version: str = "1.0.0",
        extra_parameters: list[dict[str, Any]] | None = None,
        request_body: dict[str, Any] | None = None,
        component_schema_names: tuple[str, ...] = (),
        keep_responses: bool = False,
        servers: list[dict[str, Any]] | None = None,
    ) -> "RESTToolBuilder":
        operation_id, reduced_doc = reduce_openapi_to_endpoint(
            document,
            path=path,
            method=method,
            info_title=info_title,
            info_version=info_version,
            extra_parameters=extra_parameters,
            request_body=request_body,
            component_schema_names=component_schema_names,
            keep_responses=keep_responses,
            servers=servers,
        )
        return self.openapi_inline(reduced_doc).operation(operation_id)

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

    def bind_session_auth(
        self,
        *,
        cookie_input: str = "cookie_header",
        csrf_input: str = "csrf_token",
        cookie_header_name: str = "Cookie",
        csrf_header_name: str = "X-CSRFToken",
    ) -> "RESTToolBuilder":
        return self.bind_init(cookie_input).to_header(cookie_header_name).bind_init(csrf_input).to_header(csrf_header_name)

    def allow_hostname_policy(self, hostname: str) -> "RESTToolBuilder":
        host = hostname.strip().lower()
        if not host:
            raise ValueError("hostname is required")
        return self.allow_hosts(host).allow_private_ips(host in {"localhost", "host.docker.internal", "127.0.0.1"})

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

    def censor_response_paths(self, *paths: str) -> "RESTToolBuilder":
        values: list[str] = []
        for path in paths:
            trimmed = path.strip()
            if trimmed:
                values.append(trimmed)
        self._safety_policy["response_censor_paths"] = values
        return self

    def clear_response_censor_paths(self) -> "RESTToolBuilder":
        self._safety_policy.pop("response_censor_paths", None)
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
