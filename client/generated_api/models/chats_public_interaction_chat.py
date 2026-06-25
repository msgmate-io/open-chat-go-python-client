from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chats_public_interaction_chat_interaction_details import ChatsPublicInteractionChatInteractionDetails





T = TypeVar("T", bound="ChatsPublicInteractionChat")



@_attrs_define
class ChatsPublicInteractionChat:
    """ 
        Attributes:
            chat_share_uuid (str | Unset):
            chat_type (str | Unset):
            config (Any | Unset):
            interaction_details (ChatsPublicInteractionChatInteractionDetails | Unset):
            partner (Any | Unset):
            published_at (str | Unset):
            uuid (str | Unset):
     """

    chat_share_uuid: str | Unset = UNSET
    chat_type: str | Unset = UNSET
    config: Any | Unset = UNSET
    interaction_details: ChatsPublicInteractionChatInteractionDetails | Unset = UNSET
    partner: Any | Unset = UNSET
    published_at: str | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chats_public_interaction_chat_interaction_details import ChatsPublicInteractionChatInteractionDetails
        chat_share_uuid = self.chat_share_uuid

        chat_type = self.chat_type

        config = self.config

        interaction_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.interaction_details, Unset):
            interaction_details = self.interaction_details.to_dict()

        partner = self.partner

        published_at = self.published_at

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
        if interaction_details is not UNSET:
            field_dict["interaction_details"] = interaction_details
        if partner is not UNSET:
            field_dict["partner"] = partner
        if published_at is not UNSET:
            field_dict["published_at"] = published_at
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chats_public_interaction_chat_interaction_details import ChatsPublicInteractionChatInteractionDetails
        d = dict(src_dict)
        chat_share_uuid = d.pop("chat_share_uuid", UNSET)

        chat_type = d.pop("chat_type", UNSET)

        config = d.pop("config", UNSET)

        _interaction_details = d.pop("interaction_details", UNSET)
        interaction_details: ChatsPublicInteractionChatInteractionDetails | Unset
        if isinstance(_interaction_details,  Unset):
            interaction_details = UNSET
        else:
            interaction_details = ChatsPublicInteractionChatInteractionDetails.from_dict(_interaction_details)




        partner = d.pop("partner", UNSET)

        published_at = d.pop("published_at", UNSET)

        uuid = d.pop("uuid", UNSET)

        chats_public_interaction_chat = cls(
            chat_share_uuid=chat_share_uuid,
            chat_type=chat_type,
            config=config,
            interaction_details=interaction_details,
            partner=partner,
            published_at=published_at,
            uuid=uuid,
        )


        chats_public_interaction_chat.additional_properties = d
        return chats_public_interaction_chat

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
