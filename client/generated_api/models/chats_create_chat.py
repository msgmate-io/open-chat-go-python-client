from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chats_create_chat_shared_config import ChatsCreateChatSharedConfig
  from ..models.chats_file_attachment import ChatsFileAttachment





T = TypeVar("T", bound="ChatsCreateChat")



@_attrs_define
class ChatsCreateChat:
    """ 
        Attributes:
            attachments (list[ChatsFileAttachment] | Unset):
            auto_share (bool | Unset):
            chat_type (str | Unset):
            contact_token (str | Unset):
            first_message (str | Unset):
            shared_config (ChatsCreateChatSharedConfig | Unset):
     """

    attachments: list[ChatsFileAttachment] | Unset = UNSET
    auto_share: bool | Unset = UNSET
    chat_type: str | Unset = UNSET
    contact_token: str | Unset = UNSET
    first_message: str | Unset = UNSET
    shared_config: ChatsCreateChatSharedConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chats_create_chat_shared_config import ChatsCreateChatSharedConfig
        from ..models.chats_file_attachment import ChatsFileAttachment
        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        auto_share = self.auto_share

        chat_type = self.chat_type

        contact_token = self.contact_token

        first_message = self.first_message

        shared_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shared_config, Unset):
            shared_config = self.shared_config.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if auto_share is not UNSET:
            field_dict["auto_share"] = auto_share
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
        from ..models.chats_create_chat_shared_config import ChatsCreateChatSharedConfig
        from ..models.chats_file_attachment import ChatsFileAttachment
        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: list[ChatsFileAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ChatsFileAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        auto_share = d.pop("auto_share", UNSET)

        chat_type = d.pop("chat_type", UNSET)

        contact_token = d.pop("contact_token", UNSET)

        first_message = d.pop("first_message", UNSET)

        _shared_config = d.pop("shared_config", UNSET)
        shared_config: ChatsCreateChatSharedConfig | Unset
        if isinstance(_shared_config,  Unset):
            shared_config = UNSET
        else:
            shared_config = ChatsCreateChatSharedConfig.from_dict(_shared_config)




        chats_create_chat = cls(
            attachments=attachments,
            auto_share=auto_share,
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
