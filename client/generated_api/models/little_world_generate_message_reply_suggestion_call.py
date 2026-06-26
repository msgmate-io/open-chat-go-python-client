from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="LittleWorldGenerateMessageReplySuggestionCall")



@_attrs_define
class LittleWorldGenerateMessageReplySuggestionCall:
    """ Payload for persisting the support action message suggestion; calling this tool performs the save.

        Attributes:
            message (str): Final draft support reply text that will be persisted when this tool is called.
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

        little_world_generate_message_reply_suggestion_call = cls(
            message=message,
        )

        return little_world_generate_message_reply_suggestion_call

