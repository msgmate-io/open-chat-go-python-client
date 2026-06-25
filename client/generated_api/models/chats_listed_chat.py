from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.database_message import DatabaseMessage
  from ..models.database_user import DatabaseUser





T = TypeVar("T", bound="ChatsListedChat")



@_attrs_define
class ChatsListedChat:
    """ 
        Attributes:
            chat_share_uuid (str | Unset):
            chat_type (str | Unset):
            config (Any | Unset):
            latest_message (DatabaseMessage | Unset):
            partner (DatabaseUser | Unset):
            shared_interaction_url (str | Unset):
            uuid (str | Unset):
     """

    chat_share_uuid: str | Unset = UNSET
    chat_type: str | Unset = UNSET
    config: Any | Unset = UNSET
    latest_message: DatabaseMessage | Unset = UNSET
    partner: DatabaseUser | Unset = UNSET
    shared_interaction_url: str | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.database_message import DatabaseMessage
        from ..models.database_user import DatabaseUser
        chat_share_uuid = self.chat_share_uuid

        chat_type = self.chat_type

        config = self.config

        latest_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_message, Unset):
            latest_message = self.latest_message.to_dict()

        partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partner, Unset):
            partner = self.partner.to_dict()

        shared_interaction_url = self.shared_interaction_url

        uuid = self.uuid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if chat_share_uuid is not UNSET:
            field_dict["chat_share_uuid"] = chat_share_uuid
        if chat_type is not UNSET:
            field_dict["chat_type"] = chat_type
        if config is not UNSET:
            field_dict["config"] = config
        if latest_message is not UNSET:
            field_dict["latest_message"] = latest_message
        if partner is not UNSET:
            field_dict["partner"] = partner
        if shared_interaction_url is not UNSET:
            field_dict["shared_interaction_url"] = shared_interaction_url
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_message import DatabaseMessage
        from ..models.database_user import DatabaseUser
        d = dict(src_dict)
        chat_share_uuid = d.pop("chat_share_uuid", UNSET)

        chat_type = d.pop("chat_type", UNSET)

        config = d.pop("config", UNSET)

        _latest_message = d.pop("latest_message", UNSET)
        latest_message: DatabaseMessage | Unset
        if isinstance(_latest_message,  Unset):
            latest_message = UNSET
        else:
            latest_message = DatabaseMessage.from_dict(_latest_message)




        _partner = d.pop("partner", UNSET)
        partner: DatabaseUser | Unset
        if isinstance(_partner,  Unset):
            partner = UNSET
        else:
            partner = DatabaseUser.from_dict(_partner)




        shared_interaction_url = d.pop("shared_interaction_url", UNSET)

        uuid = d.pop("uuid", UNSET)

        chats_listed_chat = cls(
            chat_share_uuid=chat_share_uuid,
            chat_type=chat_type,
            config=config,
            latest_message=latest_message,
            partner=partner,
            shared_interaction_url=shared_interaction_url,
            uuid=uuid,
        )


        chats_listed_chat.additional_properties = d
        return chats_listed_chat

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
