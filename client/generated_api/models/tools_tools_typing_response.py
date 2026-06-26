from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tools_tool_type_definition import ToolsToolTypeDefinition





T = TypeVar("T", bound="ToolsToolsTypingResponse")



@_attrs_define
class ToolsToolsTypingResponse:
    """ 
        Attributes:
            rows (list[ToolsToolTypeDefinition] | Unset):
     """

    rows: list[ToolsToolTypeDefinition] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tools_tool_type_definition import ToolsToolTypeDefinition
        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if rows is not UNSET:
            field_dict["rows"] = rows

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_tool_type_definition import ToolsToolTypeDefinition
        d = dict(src_dict)
        _rows = d.pop("rows", UNSET)
        rows: list[ToolsToolTypeDefinition] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = ToolsToolTypeDefinition.from_dict(rows_item_data)



                rows.append(rows_item)


        tools_tools_typing_response = cls(
            rows=rows,
        )


        tools_tools_typing_response.additional_properties = d
        return tools_tools_typing_response

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
