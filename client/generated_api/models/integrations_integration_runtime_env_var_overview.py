from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IntegrationsIntegrationRuntimeEnvVarOverview")



@_attrs_define
class IntegrationsIntegrationRuntimeEnvVarOverview:
    """ 
        Attributes:
            description (str | Unset):
            key (str | Unset):
            sensitive (bool | Unset):
     """

    description: str | Unset = UNSET
    key: str | Unset = UNSET
    sensitive: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        key = self.key

        sensitive = self.sensitive


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if key is not UNSET:
            field_dict["key"] = key
        if sensitive is not UNSET:
            field_dict["sensitive"] = sensitive

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        key = d.pop("key", UNSET)

        sensitive = d.pop("sensitive", UNSET)

        integrations_integration_runtime_env_var_overview = cls(
            description=description,
            key=key,
            sensitive=sensitive,
        )


        integrations_integration_runtime_env_var_overview.additional_properties = d
        return integrations_integration_runtime_env_var_overview

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
