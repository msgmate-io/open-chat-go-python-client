from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tools_tool_execution_request_input_parameters import ToolsToolExecutionRequestInputParameters





T = TypeVar("T", bound="ToolsToolExecutionRequest")



@_attrs_define
class ToolsToolExecutionRequest:
    """ 
        Attributes:
            input_parameters (ToolsToolExecutionRequestInputParameters | Unset):
     """

    input_parameters: ToolsToolExecutionRequestInputParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tools_tool_execution_request_input_parameters import ToolsToolExecutionRequestInputParameters
        input_parameters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_parameters, Unset):
            input_parameters = self.input_parameters.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if input_parameters is not UNSET:
            field_dict["input_parameters"] = input_parameters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_tool_execution_request_input_parameters import ToolsToolExecutionRequestInputParameters
        d = dict(src_dict)
        _input_parameters = d.pop("input_parameters", UNSET)
        input_parameters: ToolsToolExecutionRequestInputParameters | Unset
        if isinstance(_input_parameters,  Unset):
            input_parameters = UNSET
        else:
            input_parameters = ToolsToolExecutionRequestInputParameters.from_dict(_input_parameters)




        tools_tool_execution_request = cls(
            input_parameters=input_parameters,
        )


        tools_tool_execution_request.additional_properties = d
        return tools_tool_execution_request

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
