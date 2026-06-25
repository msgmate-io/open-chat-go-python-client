from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.models_bot_option import ModelsBotOption





T = TypeVar("T", bound="ModelsModelsFilters")



@_attrs_define
class ModelsModelsFilters:
    """ 
        Attributes:
            bots (list[ModelsBotOption] | Unset):
            hosters (list[str] | Unset):
            sources (list[str] | Unset):
     """

    bots: list[ModelsBotOption] | Unset = UNSET
    hosters: list[str] | Unset = UNSET
    sources: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.models_bot_option import ModelsBotOption
        bots: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bots, Unset):
            bots = []
            for bots_item_data in self.bots:
                bots_item = bots_item_data.to_dict()
                bots.append(bots_item)



        hosters: list[str] | Unset = UNSET
        if not isinstance(self.hosters, Unset):
            hosters = self.hosters



        sources: list[str] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bots is not UNSET:
            field_dict["bots"] = bots
        if hosters is not UNSET:
            field_dict["hosters"] = hosters
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_bot_option import ModelsBotOption
        d = dict(src_dict)
        _bots = d.pop("bots", UNSET)
        bots: list[ModelsBotOption] | Unset = UNSET
        if _bots is not UNSET:
            bots = []
            for bots_item_data in _bots:
                bots_item = ModelsBotOption.from_dict(bots_item_data)



                bots.append(bots_item)


        hosters = cast(list[str], d.pop("hosters", UNSET))


        sources = cast(list[str], d.pop("sources", UNSET))


        models_models_filters = cls(
            bots=bots,
            hosters=hosters,
            sources=sources,
        )


        models_models_filters.additional_properties = d
        return models_models_filters

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
