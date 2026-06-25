from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ModelsModelListItem")



@_attrs_define
class ModelsModelListItem:
    """ 
        Attributes:
            bots (list[str] | Unset):
            configuration (list[int] | Unset):
            description (str | Unset):
            hoster (str | Unset):
            id (int | Unset):
            model_id (str | Unset):
            source (str | Unset):
            title (str | Unset):
     """

    bots: list[str] | Unset = UNSET
    configuration: list[int] | Unset = UNSET
    description: str | Unset = UNSET
    hoster: str | Unset = UNSET
    id: int | Unset = UNSET
    model_id: str | Unset = UNSET
    source: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        bots: list[str] | Unset = UNSET
        if not isinstance(self.bots, Unset):
            bots = self.bots



        configuration: list[int] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration



        description = self.description

        hoster = self.hoster

        id = self.id

        model_id = self.model_id

        source = self.source

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bots is not UNSET:
            field_dict["bots"] = bots
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if description is not UNSET:
            field_dict["description"] = description
        if hoster is not UNSET:
            field_dict["hoster"] = hoster
        if id is not UNSET:
            field_dict["id"] = id
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if source is not UNSET:
            field_dict["source"] = source
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bots = cast(list[str], d.pop("bots", UNSET))


        configuration = cast(list[int], d.pop("configuration", UNSET))


        description = d.pop("description", UNSET)

        hoster = d.pop("hoster", UNSET)

        id = d.pop("id", UNSET)

        model_id = d.pop("model_id", UNSET)

        source = d.pop("source", UNSET)

        title = d.pop("title", UNSET)

        models_model_list_item = cls(
            bots=bots,
            configuration=configuration,
            description=description,
            hoster=hoster,
            id=id,
            model_id=model_id,
            source=source,
            title=title,
        )


        models_model_list_item.additional_properties = d
        return models_model_list_item

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
