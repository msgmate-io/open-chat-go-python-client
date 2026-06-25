from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UserUserLogin")



@_attrs_define
class UserUserLogin:
    """ 
        Attributes:
            email (str | Unset):
            password (str | Unset):
            recovery_code (str | Unset):
            two_factor_code (str | Unset):
     """

    email: str | Unset = UNSET
    password: str | Unset = UNSET
    recovery_code: str | Unset = UNSET
    two_factor_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        password = self.password

        recovery_code = self.recovery_code

        two_factor_code = self.two_factor_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if recovery_code is not UNSET:
            field_dict["recovery_code"] = recovery_code
        if two_factor_code is not UNSET:
            field_dict["two_factor_code"] = two_factor_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        recovery_code = d.pop("recovery_code", UNSET)

        two_factor_code = d.pop("two_factor_code", UNSET)

        user_user_login = cls(
            email=email,
            password=password,
            recovery_code=recovery_code,
            two_factor_code=two_factor_code,
        )


        user_user_login.additional_properties = d
        return user_user_login

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
