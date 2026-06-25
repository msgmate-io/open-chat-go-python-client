from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DatabaseUser")



@_attrs_define
class DatabaseUser:
    """ 
        Attributes:
            contact_token (str | Unset):
            is_admin (bool | Unset):
            is_automated (bool | Unset):
            name (str | Unset):
            two_factor_enabled (bool | Unset):
            uuid (str | Unset):
     """

    contact_token: str | Unset = UNSET
    is_admin: bool | Unset = UNSET
    is_automated: bool | Unset = UNSET
    name: str | Unset = UNSET
    two_factor_enabled: bool | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        contact_token = self.contact_token

        is_admin = self.is_admin

        is_automated = self.is_automated

        name = self.name

        two_factor_enabled = self.two_factor_enabled

        uuid = self.uuid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contact_token is not UNSET:
            field_dict["contact_token"] = contact_token
        if is_admin is not UNSET:
            field_dict["is_admin"] = is_admin
        if is_automated is not UNSET:
            field_dict["is_automated"] = is_automated
        if name is not UNSET:
            field_dict["name"] = name
        if two_factor_enabled is not UNSET:
            field_dict["two_factor_enabled"] = two_factor_enabled
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        contact_token = d.pop("contact_token", UNSET)

        is_admin = d.pop("is_admin", UNSET)

        is_automated = d.pop("is_automated", UNSET)

        name = d.pop("name", UNSET)

        two_factor_enabled = d.pop("two_factor_enabled", UNSET)

        uuid = d.pop("uuid", UNSET)

        database_user = cls(
            contact_token=contact_token,
            is_admin=is_admin,
            is_automated=is_automated,
            name=name,
            two_factor_enabled=two_factor_enabled,
            uuid=uuid,
        )


        database_user.additional_properties = d
        return database_user

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
