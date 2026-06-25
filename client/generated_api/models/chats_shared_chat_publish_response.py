from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatsSharedChatPublishResponse")



@_attrs_define
class ChatsSharedChatPublishResponse:
    """ 
        Attributes:
            chat_share_uuid (str | Unset):
            chat_uuid (str | Unset):
     """

    chat_share_uuid: str | Unset = UNSET
    chat_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        chat_share_uuid = self.chat_share_uuid

        chat_uuid = self.chat_uuid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chat_share_uuid is not UNSET:
            field_dict["chat_share_uuid"] = chat_share_uuid
        if chat_uuid is not UNSET:
            field_dict["chat_uuid"] = chat_uuid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_share_uuid = d.pop("chat_share_uuid", UNSET)

        chat_uuid = d.pop("chat_uuid", UNSET)

        chats_shared_chat_publish_response = cls(
            chat_share_uuid=chat_share_uuid,
            chat_uuid=chat_uuid,
        )


        chats_shared_chat_publish_response.additional_properties = d
        return chats_shared_chat_publish_response

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
