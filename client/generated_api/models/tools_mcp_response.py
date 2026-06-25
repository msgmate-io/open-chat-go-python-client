from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tools_mcp_error import ToolsMCPError





T = TypeVar("T", bound="ToolsMCPResponse")



@_attrs_define
class ToolsMCPResponse:
    """ 
        Attributes:
            error (ToolsMCPError | Unset):
            id (Any | Unset):
            jsonrpc (str | Unset):
            result (Any | Unset):
     """

    error: ToolsMCPError | Unset = UNSET
    id: Any | Unset = UNSET
    jsonrpc: str | Unset = UNSET
    result: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tools_mcp_error import ToolsMCPError
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        id = self.id

        jsonrpc = self.jsonrpc

        result = self.result


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if id is not UNSET:
            field_dict["id"] = id
        if jsonrpc is not UNSET:
            field_dict["jsonrpc"] = jsonrpc
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_mcp_error import ToolsMCPError
        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: ToolsMCPError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = ToolsMCPError.from_dict(_error)




        id = d.pop("id", UNSET)

        jsonrpc = d.pop("jsonrpc", UNSET)

        result = d.pop("result", UNSET)

        tools_mcp_response = cls(
            error=error,
            id=id,
            jsonrpc=jsonrpc,
            result=result,
        )


        tools_mcp_response.additional_properties = d
        return tools_mcp_response

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
