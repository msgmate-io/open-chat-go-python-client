from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tools_tool_execution_response_tool_info import ToolsToolExecutionResponseToolInfo





T = TypeVar("T", bound="ToolsToolExecutionResponse")



@_attrs_define
class ToolsToolExecutionResponse:
    """ 
        Attributes:
            error (str | Unset):
            result (str | Unset):
            success (bool | Unset):
            tool_info (ToolsToolExecutionResponseToolInfo | Unset):
     """

    error: str | Unset = UNSET
    result: str | Unset = UNSET
    success: bool | Unset = UNSET
    tool_info: ToolsToolExecutionResponseToolInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tools_tool_execution_response_tool_info import ToolsToolExecutionResponseToolInfo
        error = self.error

        result = self.result

        success = self.success

        tool_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_info, Unset):
            tool_info = self.tool_info.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if result is not UNSET:
            field_dict["result"] = result
        if success is not UNSET:
            field_dict["success"] = success
        if tool_info is not UNSET:
            field_dict["tool_info"] = tool_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_tool_execution_response_tool_info import ToolsToolExecutionResponseToolInfo
        d = dict(src_dict)
        error = d.pop("error", UNSET)

        result = d.pop("result", UNSET)

        success = d.pop("success", UNSET)

        _tool_info = d.pop("tool_info", UNSET)
        tool_info: ToolsToolExecutionResponseToolInfo | Unset
        if isinstance(_tool_info,  Unset):
            tool_info = UNSET
        else:
            tool_info = ToolsToolExecutionResponseToolInfo.from_dict(_tool_info)




        tools_tool_execution_response = cls(
            error=error,
            result=result,
            success=success,
            tool_info=tool_info,
        )


        tools_tool_execution_response.additional_properties = d
        return tools_tool_execution_response

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
