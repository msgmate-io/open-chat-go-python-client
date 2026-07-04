from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.restapitoolintegration_dynamic_rest_tool_detail_response_call_schema import RestapitoolintegrationDynamicRESTToolDetailResponseCallSchema
  from ..models.restapitoolintegration_dynamic_rest_tool_detail_response_init_schema import RestapitoolintegrationDynamicRESTToolDetailResponseInitSchema
  from ..models.restapitoolintegration_dynamic_rest_tool_list_row import RestapitoolintegrationDynamicRESTToolListRow





T = TypeVar("T", bound="RestapitoolintegrationDynamicRESTToolDetailResponse")



@_attrs_define
class RestapitoolintegrationDynamicRESTToolDetailResponse:
    """ 
        Attributes:
            call_schema (RestapitoolintegrationDynamicRESTToolDetailResponseCallSchema | Unset):
            init_schema (RestapitoolintegrationDynamicRESTToolDetailResponseInitSchema | Unset):
            row (RestapitoolintegrationDynamicRESTToolListRow | Unset):
     """

    call_schema: RestapitoolintegrationDynamicRESTToolDetailResponseCallSchema | Unset = UNSET
    init_schema: RestapitoolintegrationDynamicRESTToolDetailResponseInitSchema | Unset = UNSET
    row: RestapitoolintegrationDynamicRESTToolListRow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.restapitoolintegration_dynamic_rest_tool_detail_response_call_schema import RestapitoolintegrationDynamicRESTToolDetailResponseCallSchema
        from ..models.restapitoolintegration_dynamic_rest_tool_detail_response_init_schema import RestapitoolintegrationDynamicRESTToolDetailResponseInitSchema
        from ..models.restapitoolintegration_dynamic_rest_tool_list_row import RestapitoolintegrationDynamicRESTToolListRow
        call_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.call_schema, Unset):
            call_schema = self.call_schema.to_dict()

        init_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.init_schema, Unset):
            init_schema = self.init_schema.to_dict()

        row: dict[str, Any] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = self.row.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if call_schema is not UNSET:
            field_dict["call_schema"] = call_schema
        if init_schema is not UNSET:
            field_dict["init_schema"] = init_schema
        if row is not UNSET:
            field_dict["row"] = row

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.restapitoolintegration_dynamic_rest_tool_detail_response_call_schema import RestapitoolintegrationDynamicRESTToolDetailResponseCallSchema
        from ..models.restapitoolintegration_dynamic_rest_tool_detail_response_init_schema import RestapitoolintegrationDynamicRESTToolDetailResponseInitSchema
        from ..models.restapitoolintegration_dynamic_rest_tool_list_row import RestapitoolintegrationDynamicRESTToolListRow
        d = dict(src_dict)
        _call_schema = d.pop("call_schema", UNSET)
        call_schema: RestapitoolintegrationDynamicRESTToolDetailResponseCallSchema | Unset
        if isinstance(_call_schema,  Unset):
            call_schema = UNSET
        else:
            call_schema = RestapitoolintegrationDynamicRESTToolDetailResponseCallSchema.from_dict(_call_schema)




        _init_schema = d.pop("init_schema", UNSET)
        init_schema: RestapitoolintegrationDynamicRESTToolDetailResponseInitSchema | Unset
        if isinstance(_init_schema,  Unset):
            init_schema = UNSET
        else:
            init_schema = RestapitoolintegrationDynamicRESTToolDetailResponseInitSchema.from_dict(_init_schema)




        _row = d.pop("row", UNSET)
        row: RestapitoolintegrationDynamicRESTToolListRow | Unset
        if isinstance(_row,  Unset):
            row = UNSET
        else:
            row = RestapitoolintegrationDynamicRESTToolListRow.from_dict(_row)




        restapitoolintegration_dynamic_rest_tool_detail_response = cls(
            call_schema=call_schema,
            init_schema=init_schema,
            row=row,
        )


        restapitoolintegration_dynamic_rest_tool_detail_response.additional_properties = d
        return restapitoolintegration_dynamic_rest_tool_detail_response

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
