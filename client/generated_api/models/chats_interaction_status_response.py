from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChatsInteractionStatusResponse")



@_attrs_define
class ChatsInteractionStatusResponse:
    """ 
        Attributes:
            chat_uuid (str | Unset):
            is_active (bool | Unset):
            latest_message_finished (bool | Unset):
            latest_message_uuid (str | Unset):
            source (str | Unset):
            state (str | Unset):
     """

    chat_uuid: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    latest_message_finished: bool | Unset = UNSET
    latest_message_uuid: str | Unset = UNSET
    source: str | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        chat_uuid = self.chat_uuid

        is_active = self.is_active

        latest_message_finished = self.latest_message_finished

        latest_message_uuid = self.latest_message_uuid

        source = self.source

        state = self.state


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chat_uuid is not UNSET:
            field_dict["chat_uuid"] = chat_uuid
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if latest_message_finished is not UNSET:
            field_dict["latest_message_finished"] = latest_message_finished
        if latest_message_uuid is not UNSET:
            field_dict["latest_message_uuid"] = latest_message_uuid
        if source is not UNSET:
            field_dict["source"] = source
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        chat_uuid = d.pop("chat_uuid", UNSET)

        is_active = d.pop("is_active", UNSET)

        latest_message_finished = d.pop("latest_message_finished", UNSET)

        latest_message_uuid = d.pop("latest_message_uuid", UNSET)

        source = d.pop("source", UNSET)

        state = d.pop("state", UNSET)

        chats_interaction_status_response = cls(
            chat_uuid=chat_uuid,
            is_active=is_active,
            latest_message_finished=latest_message_finished,
            latest_message_uuid=latest_message_uuid,
            source=source,
            state=state,
        )


        chats_interaction_status_response.additional_properties = d
        return chats_interaction_status_response

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
