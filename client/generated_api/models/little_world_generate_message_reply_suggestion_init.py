from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="LittleWorldGenerateMessageReplySuggestionInit")



@_attrs_define
class LittleWorldGenerateMessageReplySuggestionInit:
    """ Initialization data required to authenticate and target one specific Little World support task action.

        Attributes:
            action_id (str): Identifier of the open support task action to update.
            api_host (str): Base URL of the Little World API host, for example https://app.littleworld.com.
            csrf_token (str): CSRF token paired with the session for Little World API calls.
            session_id (str): Session cookie value used to authenticate the Little World API request.
            task_pk (str): Primary key of the support task that owns the action draft.
            mock_run (bool | Unset): Optional testing flag. If true, skip the API request and return a mocked success
                result.
     """

    action_id: str
    api_host: str
    csrf_token: str
    session_id: str
    task_pk: str
    mock_run: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        action_id = self.action_id

        api_host = self.api_host

        csrf_token = self.csrf_token

        session_id = self.session_id

        task_pk = self.task_pk

        mock_run = self.mock_run


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "action_id": action_id,
            "api_host": api_host,
            "csrf_token": csrf_token,
            "session_id": session_id,
            "task_pk": task_pk,
        })
        if mock_run is not UNSET:
            field_dict["mock_run"] = mock_run

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_id = d.pop("action_id")

        api_host = d.pop("api_host")

        csrf_token = d.pop("csrf_token")

        session_id = d.pop("session_id")

        task_pk = d.pop("task_pk")

        mock_run = d.pop("mock_run", UNSET)

        little_world_generate_message_reply_suggestion_init = cls(
            action_id=action_id,
            api_host=api_host,
            csrf_token=csrf_token,
            session_id=session_id,
            task_pk=task_pk,
            mock_run=mock_run,
        )

        return little_world_generate_message_reply_suggestion_init

