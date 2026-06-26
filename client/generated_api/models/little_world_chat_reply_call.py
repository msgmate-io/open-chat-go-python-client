from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="LittleWorldChatReplyCall")



@_attrs_define
class LittleWorldChatReplyCall:
    """ Payload for sending one support response message.

        Attributes:
            message (str): The exact chat response text to send to the Little World user.
     """

    message: str





    def to_dict(self) -> dict[str, Any]:
        message = self.message


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message")

        little_world_chat_reply_call = cls(
            message=message,
        )

        return little_world_chat_reply_call

