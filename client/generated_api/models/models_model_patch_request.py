from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ModelsModelPatchRequest")



@_attrs_define
class ModelsModelPatchRequest:
    """ 
        Attributes:
            configuration (list[int] | Unset):
            description (str | Unset):
            is_public (bool | Unset):
            model_id (str | Unset):
            title (str | Unset):
     """

    configuration: list[int] | Unset = UNSET
    description: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    model_id: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        configuration: list[int] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration



        description = self.description

        is_public = self.is_public

        model_id = self.model_id

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if description is not UNSET:
            field_dict["description"] = description
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if model_id is not UNSET:
            field_dict["model_id"] = model_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configuration = cast(list[int], d.pop("configuration", UNSET))


        description = d.pop("description", UNSET)

        is_public = d.pop("is_public", UNSET)

        model_id = d.pop("model_id", UNSET)

        title = d.pop("title", UNSET)

        models_model_patch_request = cls(
            configuration=configuration,
            description=description,
            is_public=is_public,
            model_id=model_id,
            title=title,
        )


        models_model_patch_request.additional_properties = d
        return models_model_patch_request

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
