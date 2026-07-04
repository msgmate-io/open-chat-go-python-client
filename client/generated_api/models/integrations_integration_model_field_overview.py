from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IntegrationsIntegrationModelFieldOverview")



@_attrs_define
class IntegrationsIntegrationModelFieldOverview:
    """ 
        Attributes:
            fields (list[IntegrationsIntegrationModelFieldOverview] | Unset):
            json_name (str | Unset):
            kind (str | Unset):
            name (str | Unset):
            required (bool | Unset):
            type_ (str | Unset):
     """

    fields: list[IntegrationsIntegrationModelFieldOverview] | Unset = UNSET
    json_name: str | Unset = UNSET
    kind: str | Unset = UNSET
    name: str | Unset = UNSET
    required: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)



        json_name = self.json_name

        kind = self.kind

        name = self.name

        required = self.required

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if json_name is not UNSET:
            field_dict["json_name"] = json_name
        if kind is not UNSET:
            field_dict["kind"] = kind
        if name is not UNSET:
            field_dict["name"] = name
        if required is not UNSET:
            field_dict["required"] = required
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: list[IntegrationsIntegrationModelFieldOverview] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = IntegrationsIntegrationModelFieldOverview.from_dict(fields_item_data)



                fields.append(fields_item)


        json_name = d.pop("json_name", UNSET)

        kind = d.pop("kind", UNSET)

        name = d.pop("name", UNSET)

        required = d.pop("required", UNSET)

        type_ = d.pop("type", UNSET)

        integrations_integration_model_field_overview = cls(
            fields=fields,
            json_name=json_name,
            kind=kind,
            name=name,
            required=required,
            type_=type_,
        )


        integrations_integration_model_field_overview.additional_properties = d
        return integrations_integration_model_field_overview

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
