from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.integrations_integration_model_field_overview import IntegrationsIntegrationModelFieldOverview





T = TypeVar("T", bound="IntegrationsIntegrationModelOverview")



@_attrs_define
class IntegrationsIntegrationModelOverview:
    """ 
        Attributes:
            fields (list[IntegrationsIntegrationModelFieldOverview] | Unset):
            kind (str | Unset):
            type_name (str | Unset):
     """

    fields: list[IntegrationsIntegrationModelFieldOverview] | Unset = UNSET
    kind: str | Unset = UNSET
    type_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.integrations_integration_model_field_overview import IntegrationsIntegrationModelFieldOverview
        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)



        kind = self.kind

        type_name = self.type_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if kind is not UNSET:
            field_dict["kind"] = kind
        if type_name is not UNSET:
            field_dict["type_name"] = type_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.integrations_integration_model_field_overview import IntegrationsIntegrationModelFieldOverview
        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: list[IntegrationsIntegrationModelFieldOverview] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = IntegrationsIntegrationModelFieldOverview.from_dict(fields_item_data)



                fields.append(fields_item)


        kind = d.pop("kind", UNSET)

        type_name = d.pop("type_name", UNSET)

        integrations_integration_model_overview = cls(
            fields=fields,
            kind=kind,
            type_name=type_name,
        )


        integrations_integration_model_overview.additional_properties = d
        return integrations_integration_model_overview

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
