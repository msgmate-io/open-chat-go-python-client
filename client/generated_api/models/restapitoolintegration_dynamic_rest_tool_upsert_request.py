from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.restapitoolintegration_dynamic_rest_tool_upsert_request_param_bindings_item import RestapitoolintegrationDynamicRESTToolUpsertRequestParamBindingsItem
  from ..models.restapitoolintegration_dynamic_rest_tool_upsert_request_safety_policy import RestapitoolintegrationDynamicRESTToolUpsertRequestSafetyPolicy





T = TypeVar("T", bound="RestapitoolintegrationDynamicRESTToolUpsertRequest")



@_attrs_define
class RestapitoolintegrationDynamicRESTToolUpsertRequest:
    """ 
        Attributes:
            admin_only (bool | Unset):
            base_url_input_name (str | Unset):
            base_url_source (str | Unset):
            confirmation_block_message (str | Unset):
            description (str | Unset):
            enabled (bool | Unset):
            function_name (str | Unset):
            http_method (str | Unset):
            name (str | Unset):
            openapi_source (str | Unset):
            openapi_source_type (str | Unset):
            operation_id (str | Unset):
            param_bindings (list[RestapitoolintegrationDynamicRESTToolUpsertRequestParamBindingsItem] | Unset):
            path (str | Unset):
            requires_confirmation (bool | Unset):
            safety_policy (RestapitoolintegrationDynamicRESTToolUpsertRequestSafetyPolicy | Unset):
            stop_on_first_confirmable_tool_call (bool | Unset):
     """

    admin_only: bool | Unset = UNSET
    base_url_input_name: str | Unset = UNSET
    base_url_source: str | Unset = UNSET
    confirmation_block_message: str | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    function_name: str | Unset = UNSET
    http_method: str | Unset = UNSET
    name: str | Unset = UNSET
    openapi_source: str | Unset = UNSET
    openapi_source_type: str | Unset = UNSET
    operation_id: str | Unset = UNSET
    param_bindings: list[RestapitoolintegrationDynamicRESTToolUpsertRequestParamBindingsItem] | Unset = UNSET
    path: str | Unset = UNSET
    requires_confirmation: bool | Unset = UNSET
    safety_policy: RestapitoolintegrationDynamicRESTToolUpsertRequestSafetyPolicy | Unset = UNSET
    stop_on_first_confirmable_tool_call: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.restapitoolintegration_dynamic_rest_tool_upsert_request_param_bindings_item import RestapitoolintegrationDynamicRESTToolUpsertRequestParamBindingsItem
        from ..models.restapitoolintegration_dynamic_rest_tool_upsert_request_safety_policy import RestapitoolintegrationDynamicRESTToolUpsertRequestSafetyPolicy
        admin_only = self.admin_only

        base_url_input_name = self.base_url_input_name

        base_url_source = self.base_url_source

        confirmation_block_message = self.confirmation_block_message

        description = self.description

        enabled = self.enabled

        function_name = self.function_name

        http_method = self.http_method

        name = self.name

        openapi_source = self.openapi_source

        openapi_source_type = self.openapi_source_type

        operation_id = self.operation_id

        param_bindings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.param_bindings, Unset):
            param_bindings = []
            for param_bindings_item_data in self.param_bindings:
                param_bindings_item = param_bindings_item_data.to_dict()
                param_bindings.append(param_bindings_item)



        path = self.path

        requires_confirmation = self.requires_confirmation

        safety_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.safety_policy, Unset):
            safety_policy = self.safety_policy.to_dict()

        stop_on_first_confirmable_tool_call = self.stop_on_first_confirmable_tool_call


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if admin_only is not UNSET:
            field_dict["admin_only"] = admin_only
        if base_url_input_name is not UNSET:
            field_dict["base_url_input_name"] = base_url_input_name
        if base_url_source is not UNSET:
            field_dict["base_url_source"] = base_url_source
        if confirmation_block_message is not UNSET:
            field_dict["confirmation_block_message"] = confirmation_block_message
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if function_name is not UNSET:
            field_dict["function_name"] = function_name
        if http_method is not UNSET:
            field_dict["http_method"] = http_method
        if name is not UNSET:
            field_dict["name"] = name
        if openapi_source is not UNSET:
            field_dict["openapi_source"] = openapi_source
        if openapi_source_type is not UNSET:
            field_dict["openapi_source_type"] = openapi_source_type
        if operation_id is not UNSET:
            field_dict["operation_id"] = operation_id
        if param_bindings is not UNSET:
            field_dict["param_bindings"] = param_bindings
        if path is not UNSET:
            field_dict["path"] = path
        if requires_confirmation is not UNSET:
            field_dict["requires_confirmation"] = requires_confirmation
        if safety_policy is not UNSET:
            field_dict["safety_policy"] = safety_policy
        if stop_on_first_confirmable_tool_call is not UNSET:
            field_dict["stop_on_first_confirmable_tool_call"] = stop_on_first_confirmable_tool_call

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restapitoolintegration_dynamic_rest_tool_upsert_request_param_bindings_item import RestapitoolintegrationDynamicRESTToolUpsertRequestParamBindingsItem
        from ..models.restapitoolintegration_dynamic_rest_tool_upsert_request_safety_policy import RestapitoolintegrationDynamicRESTToolUpsertRequestSafetyPolicy
        d = dict(src_dict)
        admin_only = d.pop("admin_only", UNSET)

        base_url_input_name = d.pop("base_url_input_name", UNSET)

        base_url_source = d.pop("base_url_source", UNSET)

        confirmation_block_message = d.pop("confirmation_block_message", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        function_name = d.pop("function_name", UNSET)

        http_method = d.pop("http_method", UNSET)

        name = d.pop("name", UNSET)

        openapi_source = d.pop("openapi_source", UNSET)

        openapi_source_type = d.pop("openapi_source_type", UNSET)

        operation_id = d.pop("operation_id", UNSET)

        _param_bindings = d.pop("param_bindings", UNSET)
        param_bindings: list[RestapitoolintegrationDynamicRESTToolUpsertRequestParamBindingsItem] | Unset = UNSET
        if _param_bindings is not UNSET:
            param_bindings = []
            for param_bindings_item_data in _param_bindings:
                param_bindings_item = RestapitoolintegrationDynamicRESTToolUpsertRequestParamBindingsItem.from_dict(param_bindings_item_data)



                param_bindings.append(param_bindings_item)


        path = d.pop("path", UNSET)

        requires_confirmation = d.pop("requires_confirmation", UNSET)

        _safety_policy = d.pop("safety_policy", UNSET)
        safety_policy: RestapitoolintegrationDynamicRESTToolUpsertRequestSafetyPolicy | Unset
        if isinstance(_safety_policy,  Unset):
            safety_policy = UNSET
        else:
            safety_policy = RestapitoolintegrationDynamicRESTToolUpsertRequestSafetyPolicy.from_dict(_safety_policy)




        stop_on_first_confirmable_tool_call = d.pop("stop_on_first_confirmable_tool_call", UNSET)

        restapitoolintegration_dynamic_rest_tool_upsert_request = cls(
            admin_only=admin_only,
            base_url_input_name=base_url_input_name,
            base_url_source=base_url_source,
            confirmation_block_message=confirmation_block_message,
            description=description,
            enabled=enabled,
            function_name=function_name,
            http_method=http_method,
            name=name,
            openapi_source=openapi_source,
            openapi_source_type=openapi_source_type,
            operation_id=operation_id,
            param_bindings=param_bindings,
            path=path,
            requires_confirmation=requires_confirmation,
            safety_policy=safety_policy,
            stop_on_first_confirmable_tool_call=stop_on_first_confirmable_tool_call,
        )


        restapitoolintegration_dynamic_rest_tool_upsert_request.additional_properties = d
        return restapitoolintegration_dynamic_rest_tool_upsert_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
