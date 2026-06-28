from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bots_bot_dto_default_shared_config import BotsBotDTODefaultSharedConfig





T = TypeVar("T", bound="BotsBotDTO")



@_attrs_define
class BotsBotDTO:
    """ 
        Attributes:
            bot_contact_token (str | Unset):
            bot_user_uuid (str | Unset):
            bot_username (str | Unset):
            default_shared_config (BotsBotDTODefaultSharedConfig | Unset):
            description (str | Unset):
            is_active (bool | Unset):
            is_public (bool | Unset):
            name (str | Unset):
            uuid (str | Unset):
     """

    bot_contact_token: str | Unset = UNSET
    bot_user_uuid: str | Unset = UNSET
    bot_username: str | Unset = UNSET
    default_shared_config: BotsBotDTODefaultSharedConfig | Unset = UNSET
    description: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    name: str | Unset = UNSET
    uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bots_bot_dto_default_shared_config import BotsBotDTODefaultSharedConfig
        bot_contact_token = self.bot_contact_token

        bot_user_uuid = self.bot_user_uuid

        bot_username = self.bot_username

        default_shared_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_shared_config, Unset):
            default_shared_config = self.default_shared_config.to_dict()

        description = self.description

        is_active = self.is_active

        is_public = self.is_public

        name = self.name

        uuid = self.uuid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bot_contact_token is not UNSET:
            field_dict["bot_contact_token"] = bot_contact_token
        if bot_user_uuid is not UNSET:
            field_dict["bot_user_uuid"] = bot_user_uuid
        if bot_username is not UNSET:
            field_dict["bot_username"] = bot_username
        if default_shared_config is not UNSET:
            field_dict["default_shared_config"] = default_shared_config
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bots_bot_dto_default_shared_config import BotsBotDTODefaultSharedConfig
        d = dict(src_dict)
        bot_contact_token = d.pop("bot_contact_token", UNSET)

        bot_user_uuid = d.pop("bot_user_uuid", UNSET)

        bot_username = d.pop("bot_username", UNSET)

        _default_shared_config = d.pop("default_shared_config", UNSET)
        default_shared_config: BotsBotDTODefaultSharedConfig | Unset
        if isinstance(_default_shared_config,  Unset):
            default_shared_config = UNSET
        else:
            default_shared_config = BotsBotDTODefaultSharedConfig.from_dict(_default_shared_config)




        description = d.pop("description", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_public = d.pop("is_public", UNSET)

        name = d.pop("name", UNSET)

        uuid = d.pop("uuid", UNSET)

        bots_bot_dto = cls(
            bot_contact_token=bot_contact_token,
            bot_user_uuid=bot_user_uuid,
            bot_username=bot_username,
            default_shared_config=default_shared_config,
            description=description,
            is_active=is_active,
            is_public=is_public,
            name=name,
            uuid=uuid,
        )


        bots_bot_dto.additional_properties = d
        return bots_bot_dto

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
