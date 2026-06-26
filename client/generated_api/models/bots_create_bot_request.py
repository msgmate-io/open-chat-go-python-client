from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bots_create_bot_request_default_shared_config import BotsCreateBotRequestDefaultSharedConfig





T = TypeVar("T", bound="BotsCreateBotRequest")



@_attrs_define
class BotsCreateBotRequest:
    """ 
        Attributes:
            default_shared_config (BotsCreateBotRequestDefaultSharedConfig | Unset):
            description (str | Unset):
            is_public (bool | Unset):
            name (str | Unset):
            password (str | Unset):
     """

    default_shared_config: BotsCreateBotRequestDefaultSharedConfig | Unset = UNSET
    description: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    name: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bots_create_bot_request_default_shared_config import BotsCreateBotRequestDefaultSharedConfig
        default_shared_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_shared_config, Unset):
            default_shared_config = self.default_shared_config.to_dict()

        description = self.description

        is_public = self.is_public

        name = self.name

        password = self.password


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if default_shared_config is not UNSET:
            field_dict["default_shared_config"] = default_shared_config
        if description is not UNSET:
            field_dict["description"] = description
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bots_create_bot_request_default_shared_config import BotsCreateBotRequestDefaultSharedConfig
        d = dict(src_dict)
        _default_shared_config = d.pop("default_shared_config", UNSET)
        default_shared_config: BotsCreateBotRequestDefaultSharedConfig | Unset
        if isinstance(_default_shared_config,  Unset):
            default_shared_config = UNSET
        else:
            default_shared_config = BotsCreateBotRequestDefaultSharedConfig.from_dict(_default_shared_config)




        description = d.pop("description", UNSET)

        is_public = d.pop("is_public", UNSET)

        name = d.pop("name", UNSET)

        password = d.pop("password", UNSET)

        bots_create_bot_request = cls(
            default_shared_config=default_shared_config,
            description=description,
            is_public=is_public,
            name=name,
            password=password,
        )


        bots_create_bot_request.additional_properties = d
        return bots_create_bot_request

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
