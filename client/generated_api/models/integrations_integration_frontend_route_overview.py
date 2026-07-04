from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IntegrationsIntegrationFrontendRouteOverview")



@_attrs_define
class IntegrationsIntegrationFrontendRouteOverview:
    """ 
        Attributes:
            asset_path (str | Unset):
            description (str | Unset):
            kind (str | Unset):
            public (bool | Unset):
            route (str | Unset):
     """

    asset_path: str | Unset = UNSET
    description: str | Unset = UNSET
    kind: str | Unset = UNSET
    public: bool | Unset = UNSET
    route: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        asset_path = self.asset_path

        description = self.description

        kind = self.kind

        public = self.public

        route = self.route


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if asset_path is not UNSET:
            field_dict["asset_path"] = asset_path
        if description is not UNSET:
            field_dict["description"] = description
        if kind is not UNSET:
            field_dict["kind"] = kind
        if public is not UNSET:
            field_dict["public"] = public
        if route is not UNSET:
            field_dict["route"] = route

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_path = d.pop("asset_path", UNSET)

        description = d.pop("description", UNSET)

        kind = d.pop("kind", UNSET)

        public = d.pop("public", UNSET)

        route = d.pop("route", UNSET)

        integrations_integration_frontend_route_overview = cls(
            asset_path=asset_path,
            description=description,
            kind=kind,
            public=public,
            route=route,
        )


        integrations_integration_frontend_route_overview.additional_properties = d
        return integrations_integration_frontend_route_overview

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
