from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RwthAachenSeminarTimsAutoPaperIncludeExcludeCall")



@_attrs_define
class RwthAachenSeminarTimsAutoPaperIncludeExcludeCall:
    """ The parameters for the tool

        Attributes:
            include (bool): Whether to include the paper
            reason (str | Unset): The reason for the decision
     """

    include: bool
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        include = self.include

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "include": include,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include = d.pop("include")

        reason = d.pop("reason", UNSET)

        rwth_aachen_seminar_tims_auto_paper_include_exclude_call = cls(
            include=include,
            reason=reason,
        )


        rwth_aachen_seminar_tims_auto_paper_include_exclude_call.additional_properties = d
        return rwth_aachen_seminar_tims_auto_paper_include_exclude_call

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
