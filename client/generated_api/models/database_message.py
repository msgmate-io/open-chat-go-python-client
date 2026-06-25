from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DatabaseMessage")



@_attrs_define
class DatabaseMessage:
    """ 
        Attributes:
            data_type (str | Unset):
            meta_data (list[int] | Unset):
            read_at (str | Unset):
            reasoning (list[str] | Unset):
            text (str | Unset):
            tool_calls (list[list[int]] | Unset):
            uuid (str | Unset):
     """

    data_type: str | Unset = UNSET
    meta_data: list[int] | Unset = UNSET
    read_at: str | Unset = UNSET
    reasoning: list[str] | Unset = UNSET
    text: str | Unset = UNSET
    tool_calls: list[list[int]] | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        data_type = self.data_type

        meta_data: list[int] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data



        read_at = self.read_at

        reasoning: list[str] | Unset = UNSET
        if not isinstance(self.reasoning, Unset):
            reasoning = self.reasoning



        text = self.text

        tool_calls: list[list[int]] | Unset = UNSET
        if not isinstance(self.tool_calls, Unset):
            tool_calls = []
            for tool_calls_item_data in self.tool_calls:
                tool_calls_item = tool_calls_item_data


                tool_calls.append(tool_calls_item)



        uuid = self.uuid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if meta_data is not UNSET:
            field_dict["meta_data"] = meta_data
        if read_at is not UNSET:
            field_dict["read_at"] = read_at
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if text is not UNSET:
            field_dict["text"] = text
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data_type = d.pop("data_type", UNSET)

        meta_data = cast(list[int], d.pop("meta_data", UNSET))


        read_at = d.pop("read_at", UNSET)

        reasoning = cast(list[str], d.pop("reasoning", UNSET))


        text = d.pop("text", UNSET)

        _tool_calls = d.pop("tool_calls", UNSET)
        tool_calls: list[list[int]] | Unset = UNSET
        if _tool_calls is not UNSET:
            tool_calls = []
            for tool_calls_item_data in _tool_calls:
                tool_calls_item = cast(list[int], tool_calls_item_data)

                tool_calls.append(tool_calls_item)


        uuid = d.pop("uuid", UNSET)

        database_message = cls(
            data_type=data_type,
            meta_data=meta_data,
            read_at=read_at,
            reasoning=reasoning,
            text=text,
            tool_calls=tool_calls,
            uuid=uuid,
        )


        database_message.additional_properties = d
        return database_message

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
