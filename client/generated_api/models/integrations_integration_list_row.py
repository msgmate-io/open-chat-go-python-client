from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IntegrationsIntegrationListRow")



@_attrs_define
class IntegrationsIntegrationListRow:
    """ 
        Attributes:
            api_route_count (int | Unset):
            frontend_route_count (int | Unset):
            function_count (int | Unset):
            has_route_registrar (bool | Unset):
            model_provider_count (int | Unset):
            name (str | Unset):
     """

    api_route_count: int | Unset = UNSET
    frontend_route_count: int | Unset = UNSET
    function_count: int | Unset = UNSET
    has_route_registrar: bool | Unset = UNSET
    model_provider_count: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_route_count = self.api_route_count

        frontend_route_count = self.frontend_route_count

        function_count = self.function_count

        has_route_registrar = self.has_route_registrar

        model_provider_count = self.model_provider_count

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if api_route_count is not UNSET:
            field_dict["api_route_count"] = api_route_count
        if frontend_route_count is not UNSET:
            field_dict["frontend_route_count"] = frontend_route_count
        if function_count is not UNSET:
            field_dict["function_count"] = function_count
        if has_route_registrar is not UNSET:
            field_dict["has_route_registrar"] = has_route_registrar
        if model_provider_count is not UNSET:
            field_dict["model_provider_count"] = model_provider_count
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_route_count = d.pop("api_route_count", UNSET)

        frontend_route_count = d.pop("frontend_route_count", UNSET)

        function_count = d.pop("function_count", UNSET)

        has_route_registrar = d.pop("has_route_registrar", UNSET)

        model_provider_count = d.pop("model_provider_count", UNSET)

        name = d.pop("name", UNSET)

        integrations_integration_list_row = cls(
            api_route_count=api_route_count,
            frontend_route_count=frontend_route_count,
            function_count=function_count,
            has_route_registrar=has_route_registrar,
            model_provider_count=model_provider_count,
            name=name,
        )


        integrations_integration_list_row.additional_properties = d
        return integrations_integration_list_row

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
