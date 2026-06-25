from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UserTwoFactorSetupResponse")



@_attrs_define
class UserTwoFactorSetupResponse:
    """ 
        Attributes:
            qr_code_url (str | Unset):
            secret (str | Unset):
     """

    qr_code_url: str | Unset = UNSET
    secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        qr_code_url = self.qr_code_url

        secret = self.secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if qr_code_url is not UNSET:
            field_dict["qr_code_url"] = qr_code_url
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qr_code_url = d.pop("qr_code_url", UNSET)

        secret = d.pop("secret", UNSET)

        user_two_factor_setup_response = cls(
            qr_code_url=qr_code_url,
            secret=secret,
        )


        user_two_factor_setup_response.additional_properties = d
        return user_two_factor_setup_response

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
