from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tools_tool_type_definition_call_schema import ToolsToolTypeDefinitionCallSchema
  from ..models.tools_tool_type_definition_init_schema import ToolsToolTypeDefinitionInitSchema





T = TypeVar("T", bound="ToolsToolTypeDefinition")



@_attrs_define
class ToolsToolTypeDefinition:
    """ 
        Attributes:
            call_schema (ToolsToolTypeDefinitionCallSchema | Unset):
            call_type_name (str | Unset):
            function_name (str | Unset):
            init_schema (ToolsToolTypeDefinitionInitSchema | Unset):
            init_type_name (str | Unset):
            name (str | Unset):
            requires_confirmation (bool | Unset):
            requires_init (bool | Unset):
            tool_init_config_path_hint (str | Unset):
            type_ (str | Unset):
     """

    call_schema: ToolsToolTypeDefinitionCallSchema | Unset = UNSET
    call_type_name: str | Unset = UNSET
    function_name: str | Unset = UNSET
    init_schema: ToolsToolTypeDefinitionInitSchema | Unset = UNSET
    init_type_name: str | Unset = UNSET
    name: str | Unset = UNSET
    requires_confirmation: bool | Unset = UNSET
    requires_init: bool | Unset = UNSET
    tool_init_config_path_hint: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tools_tool_type_definition_call_schema import ToolsToolTypeDefinitionCallSchema
        from ..models.tools_tool_type_definition_init_schema import ToolsToolTypeDefinitionInitSchema
        call_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.call_schema, Unset):
            call_schema = self.call_schema.to_dict()

        call_type_name = self.call_type_name

        function_name = self.function_name

        init_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.init_schema, Unset):
            init_schema = self.init_schema.to_dict()

        init_type_name = self.init_type_name

        name = self.name

        requires_confirmation = self.requires_confirmation

        requires_init = self.requires_init

        tool_init_config_path_hint = self.tool_init_config_path_hint

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if call_schema is not UNSET:
            field_dict["call_schema"] = call_schema
        if call_type_name is not UNSET:
            field_dict["call_type_name"] = call_type_name
        if function_name is not UNSET:
            field_dict["function_name"] = function_name
        if init_schema is not UNSET:
            field_dict["init_schema"] = init_schema
        if init_type_name is not UNSET:
            field_dict["init_type_name"] = init_type_name
        if name is not UNSET:
            field_dict["name"] = name
        if requires_confirmation is not UNSET:
            field_dict["requires_confirmation"] = requires_confirmation
        if requires_init is not UNSET:
            field_dict["requires_init"] = requires_init
        if tool_init_config_path_hint is not UNSET:
            field_dict["tool_init_config_path_hint"] = tool_init_config_path_hint
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_tool_type_definition_call_schema import ToolsToolTypeDefinitionCallSchema
        from ..models.tools_tool_type_definition_init_schema import ToolsToolTypeDefinitionInitSchema
        d = dict(src_dict)
        _call_schema = d.pop("call_schema", UNSET)
        call_schema: ToolsToolTypeDefinitionCallSchema | Unset
        if isinstance(_call_schema,  Unset):
            call_schema = UNSET
        else:
            call_schema = ToolsToolTypeDefinitionCallSchema.from_dict(_call_schema)




        call_type_name = d.pop("call_type_name", UNSET)

        function_name = d.pop("function_name", UNSET)

        _init_schema = d.pop("init_schema", UNSET)
        init_schema: ToolsToolTypeDefinitionInitSchema | Unset
        if isinstance(_init_schema,  Unset):
            init_schema = UNSET
        else:
            init_schema = ToolsToolTypeDefinitionInitSchema.from_dict(_init_schema)




        init_type_name = d.pop("init_type_name", UNSET)

        name = d.pop("name", UNSET)

        requires_confirmation = d.pop("requires_confirmation", UNSET)

        requires_init = d.pop("requires_init", UNSET)

        tool_init_config_path_hint = d.pop("tool_init_config_path_hint", UNSET)

        type_ = d.pop("type", UNSET)

        tools_tool_type_definition = cls(
            call_schema=call_schema,
            call_type_name=call_type_name,
            function_name=function_name,
            init_schema=init_schema,
            init_type_name=init_type_name,
            name=name,
            requires_confirmation=requires_confirmation,
            requires_init=requires_init,
            tool_init_config_path_hint=tool_init_config_path_hint,
            type_=type_,
        )


        tools_tool_type_definition.additional_properties = d
        return tools_tool_type_definition

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
