from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.integrations_integration_api_route_overview import IntegrationsIntegrationAPIRouteOverview
  from ..models.integrations_integration_frontend_route_overview import IntegrationsIntegrationFrontendRouteOverview
  from ..models.integrations_integration_model_overview import IntegrationsIntegrationModelOverview





T = TypeVar("T", bound="IntegrationsIntegrationOverviewResponse")



@_attrs_define
class IntegrationsIntegrationOverviewResponse:
    """ 
        Attributes:
            api_routes (list[str] | Unset):
            api_routes_overview (list[IntegrationsIntegrationAPIRouteOverview] | Unset):
            frontend_routes (list[IntegrationsIntegrationFrontendRouteOverview] | Unset):
            functions (list[str] | Unset):
            models (list[IntegrationsIntegrationModelOverview] | Unset):
            name (str | Unset):
            readme_markdown (str | Unset):
     """

    api_routes: list[str] | Unset = UNSET
    api_routes_overview: list[IntegrationsIntegrationAPIRouteOverview] | Unset = UNSET
    frontend_routes: list[IntegrationsIntegrationFrontendRouteOverview] | Unset = UNSET
    functions: list[str] | Unset = UNSET
    models: list[IntegrationsIntegrationModelOverview] | Unset = UNSET
    name: str | Unset = UNSET
    readme_markdown: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.integrations_integration_api_route_overview import IntegrationsIntegrationAPIRouteOverview
        from ..models.integrations_integration_frontend_route_overview import IntegrationsIntegrationFrontendRouteOverview
        from ..models.integrations_integration_model_overview import IntegrationsIntegrationModelOverview
        api_routes: list[str] | Unset = UNSET
        if not isinstance(self.api_routes, Unset):
            api_routes = self.api_routes



        api_routes_overview: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.api_routes_overview, Unset):
            api_routes_overview = []
            for api_routes_overview_item_data in self.api_routes_overview:
                api_routes_overview_item = api_routes_overview_item_data.to_dict()
                api_routes_overview.append(api_routes_overview_item)



        frontend_routes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.frontend_routes, Unset):
            frontend_routes = []
            for frontend_routes_item_data in self.frontend_routes:
                frontend_routes_item = frontend_routes_item_data.to_dict()
                frontend_routes.append(frontend_routes_item)



        functions: list[str] | Unset = UNSET
        if not isinstance(self.functions, Unset):
            functions = self.functions



        models: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.models, Unset):
            models = []
            for models_item_data in self.models:
                models_item = models_item_data.to_dict()
                models.append(models_item)



        name = self.name

        readme_markdown = self.readme_markdown


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if api_routes is not UNSET:
            field_dict["api_routes"] = api_routes
        if api_routes_overview is not UNSET:
            field_dict["api_routes_overview"] = api_routes_overview
        if frontend_routes is not UNSET:
            field_dict["frontend_routes"] = frontend_routes
        if functions is not UNSET:
            field_dict["functions"] = functions
        if models is not UNSET:
            field_dict["models"] = models
        if name is not UNSET:
            field_dict["name"] = name
        if readme_markdown is not UNSET:
            field_dict["readme_markdown"] = readme_markdown

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integrations_integration_api_route_overview import IntegrationsIntegrationAPIRouteOverview
        from ..models.integrations_integration_frontend_route_overview import IntegrationsIntegrationFrontendRouteOverview
        from ..models.integrations_integration_model_overview import IntegrationsIntegrationModelOverview
        d = dict(src_dict)
        api_routes = cast(list[str], d.pop("api_routes", UNSET))


        _api_routes_overview = d.pop("api_routes_overview", UNSET)
        api_routes_overview: list[IntegrationsIntegrationAPIRouteOverview] | Unset = UNSET
        if _api_routes_overview is not UNSET:
            api_routes_overview = []
            for api_routes_overview_item_data in _api_routes_overview:
                api_routes_overview_item = IntegrationsIntegrationAPIRouteOverview.from_dict(api_routes_overview_item_data)



                api_routes_overview.append(api_routes_overview_item)


        _frontend_routes = d.pop("frontend_routes", UNSET)
        frontend_routes: list[IntegrationsIntegrationFrontendRouteOverview] | Unset = UNSET
        if _frontend_routes is not UNSET:
            frontend_routes = []
            for frontend_routes_item_data in _frontend_routes:
                frontend_routes_item = IntegrationsIntegrationFrontendRouteOverview.from_dict(frontend_routes_item_data)



                frontend_routes.append(frontend_routes_item)


        functions = cast(list[str], d.pop("functions", UNSET))


        _models = d.pop("models", UNSET)
        models: list[IntegrationsIntegrationModelOverview] | Unset = UNSET
        if _models is not UNSET:
            models = []
            for models_item_data in _models:
                models_item = IntegrationsIntegrationModelOverview.from_dict(models_item_data)



                models.append(models_item)


        name = d.pop("name", UNSET)

        readme_markdown = d.pop("readme_markdown", UNSET)

        integrations_integration_overview_response = cls(
            api_routes=api_routes,
            api_routes_overview=api_routes_overview,
            frontend_routes=frontend_routes,
            functions=functions,
            models=models,
            name=name,
            readme_markdown=readme_markdown,
        )


        integrations_integration_overview_response.additional_properties = d
        return integrations_integration_overview_response

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
