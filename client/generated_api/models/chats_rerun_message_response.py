from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatsRerunMessageResponse")



@_attrs_define
class ChatsRerunMessageResponse:
    """ 
        Attributes:
            chat_uuid (str | Unset):
            deleted_count (int | Unset):
            enqueued (bool | Unset):
            resent_message_uuid (str | Unset):
            source_message_uuid (str | Unset):
            success (bool | Unset):
     """

    chat_uuid: str | Unset = UNSET
    deleted_count: int | Unset = UNSET
    enqueued: bool | Unset = UNSET
    resent_message_uuid: str | Unset = UNSET
    source_message_uuid: str | Unset = UNSET
    success: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        chat_uuid = self.chat_uuid

        deleted_count = self.deleted_count

        enqueued = self.enqueued

        resent_message_uuid = self.resent_message_uuid

        source_message_uuid = self.source_message_uuid

        success = self.success


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chat_uuid is not UNSET:
            field_dict["chat_uuid"] = chat_uuid
        if deleted_count is not UNSET:
            field_dict["deleted_count"] = deleted_count
        if enqueued is not UNSET:
            field_dict["enqueued"] = enqueued
        if resent_message_uuid is not UNSET:
            field_dict["resent_message_uuid"] = resent_message_uuid
        if source_message_uuid is not UNSET:
            field_dict["source_message_uuid"] = source_message_uuid
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_uuid = d.pop("chat_uuid", UNSET)

        deleted_count = d.pop("deleted_count", UNSET)

        enqueued = d.pop("enqueued", UNSET)

        resent_message_uuid = d.pop("resent_message_uuid", UNSET)

        source_message_uuid = d.pop("source_message_uuid", UNSET)

        success = d.pop("success", UNSET)

        chats_rerun_message_response = cls(
            chat_uuid=chat_uuid,
            deleted_count=deleted_count,
            enqueued=enqueued,
            resent_message_uuid=resent_message_uuid,
            source_message_uuid=source_message_uuid,
            success=success,
        )


        chats_rerun_message_response.additional_properties = d
        return chats_rerun_message_response

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
