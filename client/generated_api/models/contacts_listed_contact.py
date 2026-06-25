from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.contacts_listed_contact_profile_data import ContactsListedContactProfileData





T = TypeVar("T", bound="ContactsListedContact")



@_attrs_define
class ContactsListedContact:
    """ 
        Attributes:
            contact_token (str | Unset):
            is_automated (bool | Unset):
            is_online (bool | Unset):
            name (str | Unset):
            profile_data (ContactsListedContactProfileData | Unset):
            user_uuid (str | Unset):
     """

    contact_token: str | Unset = UNSET
    is_automated: bool | Unset = UNSET
    is_online: bool | Unset = UNSET
    name: str | Unset = UNSET
    profile_data: ContactsListedContactProfileData | Unset = UNSET
    user_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.contacts_listed_contact_profile_data import ContactsListedContactProfileData
        contact_token = self.contact_token

        is_automated = self.is_automated

        is_online = self.is_online

        name = self.name

        profile_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile_data, Unset):
            profile_data = self.profile_data.to_dict()

        user_uuid = self.user_uuid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contact_token is not UNSET:
            field_dict["contact_token"] = contact_token
        if is_automated is not UNSET:
            field_dict["is_automated"] = is_automated
        if is_online is not UNSET:
            field_dict["is_online"] = is_online
        if name is not UNSET:
            field_dict["name"] = name
        if profile_data is not UNSET:
            field_dict["profile_data"] = profile_data
        if user_uuid is not UNSET:
            field_dict["user_uuid"] = user_uuid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contacts_listed_contact_profile_data import ContactsListedContactProfileData
        d = dict(src_dict)
        contact_token = d.pop("contact_token", UNSET)

        is_automated = d.pop("is_automated", UNSET)

        is_online = d.pop("is_online", UNSET)

        name = d.pop("name", UNSET)

        _profile_data = d.pop("profile_data", UNSET)
        profile_data: ContactsListedContactProfileData | Unset
        if isinstance(_profile_data,  Unset):
            profile_data = UNSET
        else:
            profile_data = ContactsListedContactProfileData.from_dict(_profile_data)




        user_uuid = d.pop("user_uuid", UNSET)

        contacts_listed_contact = cls(
            contact_token=contact_token,
            is_automated=is_automated,
            is_online=is_online,
            name=name,
            profile_data=profile_data,
            user_uuid=user_uuid,
        )


        contacts_listed_contact.additional_properties = d
        return contacts_listed_contact

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
