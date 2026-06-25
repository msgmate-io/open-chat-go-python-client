from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tools_tool_list_item_call_schema import ToolsToolListItemCallSchema
  from ..models.tools_tool_list_item_init_schema import ToolsToolListItemInitSchema
  from ..models.tools_tool_list_item_parameters import ToolsToolListItemParameters





T = TypeVar("T", bound="ToolsToolListItem")



@_attrs_define
class ToolsToolListItem:
    """ 
        Attributes:
            call_schema (ToolsToolListItemCallSchema | Unset):
            confirmation_block_message (str | Unset):
            description (str | Unset):
            function_name (str | Unset):
            init_schema (ToolsToolListItemInitSchema | Unset):
            name (str | Unset):
            parameters (ToolsToolListItemParameters | Unset):
            required (list[str] | Unset):
            requires_confirmation (bool | Unset):
            requires_init (bool | Unset):
            source_line (int | Unset):
            source_path (str | Unset):
            source_url (str | Unset):
            stop_on_first_confirmable_tool_call (bool | Unset):
            type_ (str | Unset):
     """

    call_schema: ToolsToolListItemCallSchema | Unset = UNSET
    confirmation_block_message: str | Unset = UNSET
    description: str | Unset = UNSET
    function_name: str | Unset = UNSET
    init_schema: ToolsToolListItemInitSchema | Unset = UNSET
    name: str | Unset = UNSET
    parameters: ToolsToolListItemParameters | Unset = UNSET
    required: list[str] | Unset = UNSET
    requires_confirmation: bool | Unset = UNSET
    requires_init: bool | Unset = UNSET
    source_line: int | Unset = UNSET
    source_path: str | Unset = UNSET
    source_url: str | Unset = UNSET
    stop_on_first_confirmable_tool_call: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tools_tool_list_item_call_schema import ToolsToolListItemCallSchema
        from ..models.tools_tool_list_item_init_schema import ToolsToolListItemInitSchema
        from ..models.tools_tool_list_item_parameters import ToolsToolListItemParameters
        call_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.call_schema, Unset):
            call_schema = self.call_schema.to_dict()

        confirmation_block_message = self.confirmation_block_message

        description = self.description

        function_name = self.function_name

        init_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.init_schema, Unset):
            init_schema = self.init_schema.to_dict()

        name = self.name

        parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        required: list[str] | Unset = UNSET
        if not isinstance(self.required, Unset):
            required = self.required



        requires_confirmation = self.requires_confirmation

        requires_init = self.requires_init

        source_line = self.source_line

        source_path = self.source_path

        source_url = self.source_url

        stop_on_first_confirmable_tool_call = self.stop_on_first_confirmable_tool_call

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if call_schema is not UNSET:
            field_dict["call_schema"] = call_schema
        if confirmation_block_message is not UNSET:
            field_dict["confirmation_block_message"] = confirmation_block_message
        if description is not UNSET:
            field_dict["description"] = description
        if function_name is not UNSET:
            field_dict["function_name"] = function_name
        if init_schema is not UNSET:
            field_dict["init_schema"] = init_schema
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if required is not UNSET:
            field_dict["required"] = required
        if requires_confirmation is not UNSET:
            field_dict["requires_confirmation"] = requires_confirmation
        if requires_init is not UNSET:
            field_dict["requires_init"] = requires_init
        if source_line is not UNSET:
            field_dict["source_line"] = source_line
        if source_path is not UNSET:
            field_dict["source_path"] = source_path
        if source_url is not UNSET:
            field_dict["source_url"] = source_url
        if stop_on_first_confirmable_tool_call is not UNSET:
            field_dict["stop_on_first_confirmable_tool_call"] = stop_on_first_confirmable_tool_call
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_tool_list_item_call_schema import ToolsToolListItemCallSchema
        from ..models.tools_tool_list_item_init_schema import ToolsToolListItemInitSchema
        from ..models.tools_tool_list_item_parameters import ToolsToolListItemParameters
        d = dict(src_dict)
        _call_schema = d.pop("call_schema", UNSET)
        call_schema: ToolsToolListItemCallSchema | Unset
        if isinstance(_call_schema,  Unset):
            call_schema = UNSET
        else:
            call_schema = ToolsToolListItemCallSchema.from_dict(_call_schema)




        confirmation_block_message = d.pop("confirmation_block_message", UNSET)

        description = d.pop("description", UNSET)

        function_name = d.pop("function_name", UNSET)

        _init_schema = d.pop("init_schema", UNSET)
        init_schema: ToolsToolListItemInitSchema | Unset
        if isinstance(_init_schema,  Unset):
            init_schema = UNSET
        else:
            init_schema = ToolsToolListItemInitSchema.from_dict(_init_schema)




        name = d.pop("name", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: ToolsToolListItemParameters | Unset
        if isinstance(_parameters,  Unset):
            parameters = UNSET
        else:
            parameters = ToolsToolListItemParameters.from_dict(_parameters)




        required = cast(list[str], d.pop("required", UNSET))


        requires_confirmation = d.pop("requires_confirmation", UNSET)

        requires_init = d.pop("requires_init", UNSET)

        source_line = d.pop("source_line", UNSET)

        source_path = d.pop("source_path", UNSET)

        source_url = d.pop("source_url", UNSET)

        stop_on_first_confirmable_tool_call = d.pop("stop_on_first_confirmable_tool_call", UNSET)

        type_ = d.pop("type", UNSET)

        tools_tool_list_item = cls(
            call_schema=call_schema,
            confirmation_block_message=confirmation_block_message,
            description=description,
            function_name=function_name,
            init_schema=init_schema,
            name=name,
            parameters=parameters,
            required=required,
            requires_confirmation=requires_confirmation,
            requires_init=requires_init,
            source_line=source_line,
            source_path=source_path,
            source_url=source_url,
            stop_on_first_confirmable_tool_call=stop_on_first_confirmable_tool_call,
            type_=type_,
        )


        tools_tool_list_item.additional_properties = d
        return tools_tool_list_item

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
