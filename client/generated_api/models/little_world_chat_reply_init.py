from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="LittleWorldChatReplyInit")



@_attrs_define
class LittleWorldChatReplyInit:
    """ Initialization data required to authenticate and target the Little World chat API.

        Attributes:
            api_host (str): Base URL of the Little World API host, for example https://app.littleworld.com.
            chat_uuid (str): UUID of the target Little World support chat conversation.
            csrf_token (str): CSRF token paired with the session for Little World API calls.
            session_id (str): Session cookie value used to authenticate the Little World API request.
     """

    api_host: str
    chat_uuid: str
    csrf_token: str
    session_id: str





    def to_dict(self) -> dict[str, Any]:
        api_host = self.api_host

        chat_uuid = self.chat_uuid

        csrf_token = self.csrf_token

        session_id = self.session_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "api_host": api_host,
            "chat_uuid": chat_uuid,
            "csrf_token": csrf_token,
            "session_id": session_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_host = d.pop("api_host")

        chat_uuid = d.pop("chat_uuid")

        csrf_token = d.pop("csrf_token")

        session_id = d.pop("session_id")

        little_world_chat_reply_init = cls(
            api_host=api_host,
            chat_uuid=chat_uuid,
            csrf_token=csrf_token,
            session_id=session_id,
        )

        return little_world_chat_reply_init

