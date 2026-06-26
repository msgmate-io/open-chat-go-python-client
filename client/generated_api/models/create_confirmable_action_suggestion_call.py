from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateConfirmableActionSuggestionCall")



@_attrs_define
class CreateConfirmableActionSuggestionCall:
    """ The parameters for the tool

        Attributes:
            suggested_inputs (str): Json encoded action input suggestion (editable)
            target_tool_name (str): Name of the tool that should run after user confirmation
            confirm_label (str | Unset): Optional confirm button label
            continue_after_execute (bool | Unset): Optional: if true, continue the interaction after this action executes
            danger_level (str | Unset): Optional risk level hint: low|medium|high
            description (str | Unset): Optional explanation shown to the user before confirmation
            title (str | Unset): Optional UI title for the confirmation widget
     """

    suggested_inputs: str
    target_tool_name: str
    confirm_label: str | Unset = UNSET
    continue_after_execute: bool | Unset = UNSET
    danger_level: str | Unset = UNSET
    description: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        suggested_inputs = self.suggested_inputs

        target_tool_name = self.target_tool_name

        confirm_label = self.confirm_label

        continue_after_execute = self.continue_after_execute

        danger_level = self.danger_level

        description = self.description

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "suggested_inputs": suggested_inputs,
            "target_tool_name": target_tool_name,
        })
        if confirm_label is not UNSET:
            field_dict["confirm_label"] = confirm_label
        if continue_after_execute is not UNSET:
            field_dict["continue_after_execute"] = continue_after_execute
        if danger_level is not UNSET:
            field_dict["danger_level"] = danger_level
        if description is not UNSET:
            field_dict["description"] = description
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suggested_inputs = d.pop("suggested_inputs")

        target_tool_name = d.pop("target_tool_name")

        confirm_label = d.pop("confirm_label", UNSET)

        continue_after_execute = d.pop("continue_after_execute", UNSET)

        danger_level = d.pop("danger_level", UNSET)

        description = d.pop("description", UNSET)

        title = d.pop("title", UNSET)

        create_confirmable_action_suggestion_call = cls(
            suggested_inputs=suggested_inputs,
            target_tool_name=target_tool_name,
            confirm_label=confirm_label,
            continue_after_execute=continue_after_execute,
            danger_level=danger_level,
            description=description,
            title=title,
        )


        create_confirmable_action_suggestion_call.additional_properties = d
        return create_confirmable_action_suggestion_call

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
