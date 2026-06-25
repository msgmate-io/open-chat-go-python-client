from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chats_listed_message_meta_data import ChatsListedMessageMetaData





T = TypeVar("T", bound="ChatsListedMessage")



@_attrs_define
class ChatsListedMessage:
    """ 
        Attributes:
            data_type (str | Unset):
            meta_data (ChatsListedMessageMetaData | Unset):
            reasoning (list[str] | Unset):
            receiver_id (int | Unset):
            send_at (str | Unset):
            sender_id (int | Unset):
            sender_is_automated (bool | Unset):
            sender_uuid (str | Unset):
            text (str | Unset):
            tool_calls (list[Any] | Unset):
            uuid (str | Unset):
     """

    data_type: str | Unset = UNSET
    meta_data: ChatsListedMessageMetaData | Unset = UNSET
    reasoning: list[str] | Unset = UNSET
    receiver_id: int | Unset = UNSET
    send_at: str | Unset = UNSET
    sender_id: int | Unset = UNSET
    sender_is_automated: bool | Unset = UNSET
    sender_uuid: str | Unset = UNSET
    text: str | Unset = UNSET
    tool_calls: list[Any] | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chats_listed_message_meta_data import ChatsListedMessageMetaData
        data_type = self.data_type

        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        reasoning: list[str] | Unset = UNSET
        if not isinstance(self.reasoning, Unset):
            reasoning = self.reasoning



        receiver_id = self.receiver_id

        send_at = self.send_at

        sender_id = self.sender_id

        sender_is_automated = self.sender_is_automated

        sender_uuid = self.sender_uuid

        text = self.text

        tool_calls: list[Any] | Unset = UNSET
        if not isinstance(self.tool_calls, Unset):
            tool_calls = self.tool_calls



        uuid = self.uuid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if meta_data is not UNSET:
            field_dict["meta_data"] = meta_data
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if receiver_id is not UNSET:
            field_dict["receiver_id"] = receiver_id
        if send_at is not UNSET:
            field_dict["send_at"] = send_at
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id
        if sender_is_automated is not UNSET:
            field_dict["sender_is_automated"] = sender_is_automated
        if sender_uuid is not UNSET:
            field_dict["sender_uuid"] = sender_uuid
        if text is not UNSET:
            field_dict["text"] = text
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chats_listed_message_meta_data import ChatsListedMessageMetaData
        d = dict(src_dict)
        data_type = d.pop("data_type", UNSET)

        _meta_data = d.pop("meta_data", UNSET)
        meta_data: ChatsListedMessageMetaData | Unset
        if isinstance(_meta_data,  Unset):
            meta_data = UNSET
        else:
            meta_data = ChatsListedMessageMetaData.from_dict(_meta_data)




        reasoning = cast(list[str], d.pop("reasoning", UNSET))


        receiver_id = d.pop("receiver_id", UNSET)

        send_at = d.pop("send_at", UNSET)

        sender_id = d.pop("sender_id", UNSET)

        sender_is_automated = d.pop("sender_is_automated", UNSET)

        sender_uuid = d.pop("sender_uuid", UNSET)

        text = d.pop("text", UNSET)

        tool_calls = cast(list[Any], d.pop("tool_calls", UNSET))


        uuid = d.pop("uuid", UNSET)

        chats_listed_message = cls(
            data_type=data_type,
            meta_data=meta_data,
            reasoning=reasoning,
            receiver_id=receiver_id,
            send_at=send_at,
            sender_id=sender_id,
            sender_is_automated=sender_is_automated,
            sender_uuid=sender_uuid,
            text=text,
            tool_calls=tool_calls,
            uuid=uuid,
        )


        chats_listed_message.additional_properties = d
        return chats_listed_message

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
