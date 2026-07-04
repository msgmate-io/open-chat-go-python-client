from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.integrations_integration_api_parameter_overview import IntegrationsIntegrationAPIParameterOverview





T = TypeVar("T", bound="IntegrationsIntegrationAPIRouteOverview")



@_attrs_define
class IntegrationsIntegrationAPIRouteOverview:
    """ 
        Attributes:
            description (str | Unset):
            parameters (list[IntegrationsIntegrationAPIParameterOverview] | Unset):
            required_auth (list[str] | Unset):
            route (str | Unset):
            summary (str | Unset):
     """

    description: str | Unset = UNSET
    parameters: list[IntegrationsIntegrationAPIParameterOverview] | Unset = UNSET
    required_auth: list[str] | Unset = UNSET
    route: str | Unset = UNSET
    summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.integrations_integration_api_parameter_overview import IntegrationsIntegrationAPIParameterOverview
        description = self.description

        parameters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for parameters_item_data in self.parameters:
                parameters_item = parameters_item_data.to_dict()
                parameters.append(parameters_item)



        required_auth: list[str] | Unset = UNSET
        if not isinstance(self.required_auth, Unset):
            required_auth = self.required_auth



        route = self.route

        summary = self.summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if required_auth is not UNSET:
            field_dict["required_auth"] = required_auth
        if route is not UNSET:
            field_dict["route"] = route
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integrations_integration_api_parameter_overview import IntegrationsIntegrationAPIParameterOverview
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: list[IntegrationsIntegrationAPIParameterOverview] | Unset = UNSET
        if _parameters is not UNSET:
            parameters = []
            for parameters_item_data in _parameters:
                parameters_item = IntegrationsIntegrationAPIParameterOverview.from_dict(parameters_item_data)



                parameters.append(parameters_item)


        required_auth = cast(list[str], d.pop("required_auth", UNSET))


        route = d.pop("route", UNSET)

        summary = d.pop("summary", UNSET)

        integrations_integration_api_route_overview = cls(
            description=description,
            parameters=parameters,
            required_auth=required_auth,
            route=route,
            summary=summary,
        )


        integrations_integration_api_route_overview.additional_properties = d
        return integrations_integration_api_route_overview

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
