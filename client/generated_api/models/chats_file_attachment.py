from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatsFileAttachment")



@_attrs_define
class ChatsFileAttachment:
    """ 
        Attributes:
            display_name (str | Unset):
            file_id (str | Unset):
            file_name (str | Unset):
            file_size (int | Unset):
            mime_type (str | Unset):
     """

    display_name: str | Unset = UNSET
    file_id: str | Unset = UNSET
    file_name: str | Unset = UNSET
    file_size: int | Unset = UNSET
    mime_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        file_id = self.file_id

        file_name = self.file_name

        file_size = self.file_size

        mime_type = self.mime_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        file_id = d.pop("file_id", UNSET)

        file_name = d.pop("file_name", UNSET)

        file_size = d.pop("file_size", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        chats_file_attachment = cls(
            display_name=display_name,
            file_id=file_id,
            file_name=file_name,
            file_size=file_size,
            mime_type=mime_type,
        )


        chats_file_attachment.additional_properties = d
        return chats_file_attachment

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
