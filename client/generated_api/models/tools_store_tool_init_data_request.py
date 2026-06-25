from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tools_store_tool_init_data_request_init_data import ToolsStoreToolInitDataRequestInitData





T = TypeVar("T", bound="ToolsStoreToolInitDataRequest")



@_attrs_define
class ToolsStoreToolInitDataRequest:
    """ 
        Attributes:
            expires_at (str | Unset): ISO 8601 timestamp
            init_data (ToolsStoreToolInitDataRequestInitData | Unset):
            tool_name (str | Unset):
     """

    expires_at: str | Unset = UNSET
    init_data: ToolsStoreToolInitDataRequestInitData | Unset = UNSET
    tool_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tools_store_tool_init_data_request_init_data import ToolsStoreToolInitDataRequestInitData
        expires_at = self.expires_at

        init_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.init_data, Unset):
            init_data = self.init_data.to_dict()

        tool_name = self.tool_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if init_data is not UNSET:
            field_dict["init_data"] = init_data
        if tool_name is not UNSET:
            field_dict["tool_name"] = tool_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tools_store_tool_init_data_request_init_data import ToolsStoreToolInitDataRequestInitData
        d = dict(src_dict)
        expires_at = d.pop("expires_at", UNSET)

        _init_data = d.pop("init_data", UNSET)
        init_data: ToolsStoreToolInitDataRequestInitData | Unset
        if isinstance(_init_data,  Unset):
            init_data = UNSET
        else:
            init_data = ToolsStoreToolInitDataRequestInitData.from_dict(_init_data)




        tool_name = d.pop("tool_name", UNSET)

        tools_store_tool_init_data_request = cls(
            expires_at=expires_at,
            init_data=init_data,
            tool_name=tool_name,
        )


        tools_store_tool_init_data_request.additional_properties = d
        return tools_store_tool_init_data_request

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
