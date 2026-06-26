from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PostApiV1ToolsTypingRunCallbackFunctionInitValidateResponse200")



@_attrs_define
class PostApiV1ToolsTypingRunCallbackFunctionInitValidateResponse200:
    """ 
        Attributes:
            kind (str):  Example: init.
            tool_name (str):  Example: run_callback_function.
            valid (bool):  Example: True.
     """

    kind: str
    tool_name: str
    valid: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        tool_name = self.tool_name

        valid = self.valid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "kind": kind,
            "tool_name": tool_name,
            "valid": valid,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = d.pop("kind")

        tool_name = d.pop("tool_name")

        valid = d.pop("valid")

        post_api_v1_tools_typing_run_callback_function_init_validate_response_200 = cls(
            kind=kind,
            tool_name=tool_name,
            valid=valid,
        )


        post_api_v1_tools_typing_run_callback_function_init_validate_response_200.additional_properties = d
        return post_api_v1_tools_typing_run_callback_function_init_validate_response_200

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
