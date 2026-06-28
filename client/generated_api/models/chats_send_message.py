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
  from ..models.chats_send_message_meta_data import ChatsSendMessageMetaData
  from ..models.chats_send_message_tool_init import ChatsSendMessageToolInit





T = TypeVar("T", bound="ChatsSendMessage")



@_attrs_define
class ChatsSendMessage:
    """ 
        Attributes:
            attachments (list[ChatsFileAttachment] | Unset):
            meta_data (ChatsSendMessageMetaData | Unset):
            reasoning (list[str] | Unset):
            text (str | Unset):
            tool_calls (list[Any] | Unset):
            tool_init (ChatsSendMessageToolInit | Unset):
     """

    attachments: list[ChatsFileAttachment] | Unset = UNSET
    meta_data: ChatsSendMessageMetaData | Unset = UNSET
    reasoning: list[str] | Unset = UNSET
    text: str | Unset = UNSET
    tool_calls: list[Any] | Unset = UNSET
    tool_init: ChatsSendMessageToolInit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chats_file_attachment import ChatsFileAttachment
        from ..models.chats_send_message_meta_data import ChatsSendMessageMetaData
        from ..models.chats_send_message_tool_init import ChatsSendMessageToolInit
        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        meta_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta_data, Unset):
            meta_data = self.meta_data.to_dict()

        reasoning: list[str] | Unset = UNSET
        if not isinstance(self.reasoning, Unset):
            reasoning = self.reasoning



        text = self.text

        tool_calls: list[Any] | Unset = UNSET
        if not isinstance(self.tool_calls, Unset):
            tool_calls = self.tool_calls



        tool_init: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_init, Unset):
            tool_init = self.tool_init.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if meta_data is not UNSET:
            field_dict["meta_data"] = meta_data
        if reasoning is not UNSET:
            field_dict["reasoning"] = reasoning
        if text is not UNSET:
            field_dict["text"] = text
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls
        if tool_init is not UNSET:
            field_dict["tool_init"] = tool_init

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chats_file_attachment import ChatsFileAttachment
        from ..models.chats_send_message_meta_data import ChatsSendMessageMetaData
        from ..models.chats_send_message_tool_init import ChatsSendMessageToolInit
        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: list[ChatsFileAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = ChatsFileAttachment.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        _meta_data = d.pop("meta_data", UNSET)
        meta_data: ChatsSendMessageMetaData | Unset
        if isinstance(_meta_data,  Unset):
            meta_data = UNSET
        else:
            meta_data = ChatsSendMessageMetaData.from_dict(_meta_data)




        reasoning = cast(list[str], d.pop("reasoning", UNSET))


        text = d.pop("text", UNSET)

        tool_calls = cast(list[Any], d.pop("tool_calls", UNSET))


        _tool_init = d.pop("tool_init", UNSET)
        tool_init: ChatsSendMessageToolInit | Unset
        if isinstance(_tool_init,  Unset):
            tool_init = UNSET
        else:
            tool_init = ChatsSendMessageToolInit.from_dict(_tool_init)




        chats_send_message = cls(
            attachments=attachments,
            meta_data=meta_data,
            reasoning=reasoning,
            text=text,
            tool_calls=tool_calls,
            tool_init=tool_init,
        )


        chats_send_message.additional_properties = d
        return chats_send_message

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
