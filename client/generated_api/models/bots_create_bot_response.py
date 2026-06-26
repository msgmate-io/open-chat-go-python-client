from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bots_bot_dto import BotsBotDTO





T = TypeVar("T", bound="BotsCreateBotResponse")



@_attrs_define
class BotsCreateBotResponse:
    """ 
        Attributes:
            bot (BotsBotDTO | Unset):
            generated_password (str | Unset):
     """

    bot: BotsBotDTO | Unset = UNSET
    generated_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bots_bot_dto import BotsBotDTO
        bot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bot, Unset):
            bot = self.bot.to_dict()

        generated_password = self.generated_password


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bot is not UNSET:
            field_dict["bot"] = bot
        if generated_password is not UNSET:
            field_dict["generated_password"] = generated_password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bots_bot_dto import BotsBotDTO
        d = dict(src_dict)
        _bot = d.pop("bot", UNSET)
        bot: BotsBotDTO | Unset
        if isinstance(_bot,  Unset):
            bot = UNSET
        else:
            bot = BotsBotDTO.from_dict(_bot)




        generated_password = d.pop("generated_password", UNSET)

        bots_create_bot_response = cls(
            bot=bot,
            generated_password=generated_password,
        )


        bots_create_bot_response.additional_properties = d
        return bots_create_bot_response

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
