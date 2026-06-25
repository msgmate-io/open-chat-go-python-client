from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chats_file_attachment import ChatsFileAttachment





T = TypeVar("T", bound="ChatsCreateChat")



@_attrs_define
class ChatsCreateChat:
    """ 
        Attributes:
            attachments (list[ChatsFileAttachment] | Unset):
            chat_type (str | Unset):
            contact_token (str | Unset):
            first_message (str | Unset):
            shared_config (list[int] | Unset):
     """

    attachments: list[ChatsFileAttachment] | Unset = UNSET
    chat_type: str | Unset = UNSET
    contact_token: str | Unset = UNSET
    first_message: str | Unset = UNSET
    shared_config: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chats_file_attachment import ChatsFileAttachment
        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        chat_type = self.chat_type

        contact_token = self.contact_token

        first_message = self.first_message

        shared_config: list[int] | Unset = UNSET
        if not isinstance(self.shared_config, Unset):
            shared_config = self.shared_config




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if chat_type is not UNSET:
            field_dict["chat_type"] = chat_type
        if contact_token is not UNSET:
            field_dict["contact_token"] = contact_token
        if first_message is not UNSET:
            field_dict["first_message"] = first_message
        if shared_config is not UNSET:
            field_dict["shared_config"] = shared_config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chats_file_attachment import ChatsFileAttachment
        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: list[ChatsFileAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ChatsFileAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        chat_type = d.pop("chat_type", UNSET)

        contact_token = d.pop("contact_token", UNSET)

        first_message = d.pop("first_message", UNSET)

        shared_config = cast(list[int], d.pop("shared_config", UNSET))


        chats_create_chat = cls(
            attachments=attachments,
            chat_type=chat_type,
            contact_token=contact_token,
            first_message=first_message,
            shared_config=shared_config,
        )


        chats_create_chat.additional_properties = d
        return chats_create_chat

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
