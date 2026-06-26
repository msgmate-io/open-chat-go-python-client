from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bots_create_bot_interaction_request_config_overrides import BotsCreateBotInteractionRequestConfigOverrides
  from ..models.bots_create_bot_interaction_request_tool_init import BotsCreateBotInteractionRequestToolInit





T = TypeVar("T", bound="BotsCreateBotInteractionRequest")



@_attrs_define
class BotsCreateBotInteractionRequest:
    """ 
        Attributes:
            config_overrides (BotsCreateBotInteractionRequestConfigOverrides | Unset):
            message (str | Unset):
            tool_init (BotsCreateBotInteractionRequestToolInit | Unset):
     """

    config_overrides: BotsCreateBotInteractionRequestConfigOverrides | Unset = UNSET
    message: str | Unset = UNSET
    tool_init: BotsCreateBotInteractionRequestToolInit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bots_create_bot_interaction_request_config_overrides import BotsCreateBotInteractionRequestConfigOverrides
        from ..models.bots_create_bot_interaction_request_tool_init import BotsCreateBotInteractionRequestToolInit
        config_overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config_overrides, Unset):
            config_overrides = self.config_overrides.to_dict()

        message = self.message

        tool_init: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_init, Unset):
            tool_init = self.tool_init.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if config_overrides is not UNSET:
            field_dict["config_overrides"] = config_overrides
        if message is not UNSET:
            field_dict["message"] = message
        if tool_init is not UNSET:
            field_dict["tool_init"] = tool_init

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bots_create_bot_interaction_request_config_overrides import BotsCreateBotInteractionRequestConfigOverrides
        from ..models.bots_create_bot_interaction_request_tool_init import BotsCreateBotInteractionRequestToolInit
        d = dict(src_dict)
        _config_overrides = d.pop("config_overrides", UNSET)
        config_overrides: BotsCreateBotInteractionRequestConfigOverrides | Unset
        if isinstance(_config_overrides,  Unset):
            config_overrides = UNSET
        else:
            config_overrides = BotsCreateBotInteractionRequestConfigOverrides.from_dict(_config_overrides)




        message = d.pop("message", UNSET)

        _tool_init = d.pop("tool_init", UNSET)
        tool_init: BotsCreateBotInteractionRequestToolInit | Unset
        if isinstance(_tool_init,  Unset):
            tool_init = UNSET
        else:
            tool_init = BotsCreateBotInteractionRequestToolInit.from_dict(_tool_init)




        bots_create_bot_interaction_request = cls(
            config_overrides=config_overrides,
            message=message,
            tool_init=tool_init,
        )


        bots_create_bot_interaction_request.additional_properties = d
        return bots_create_bot_interaction_request

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
