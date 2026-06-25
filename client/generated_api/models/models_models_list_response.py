from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.models_model_list_item import ModelsModelListItem
  from ..models.models_models_filters import ModelsModelsFilters





T = TypeVar("T", bound="ModelsModelsListResponse")



@_attrs_define
class ModelsModelsListResponse:
    """ 
        Attributes:
            filters (ModelsModelsFilters | Unset):
            page (int | Unset):
            page_size (int | Unset):
            rows (list[ModelsModelListItem] | Unset):
            total_pages (int | Unset):
            total_rows (int | Unset):
     """

    filters: ModelsModelsFilters | Unset = UNSET
    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    rows: list[ModelsModelListItem] | Unset = UNSET
    total_pages: int | Unset = UNSET
    total_rows: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.models_model_list_item import ModelsModelListItem
        from ..models.models_models_filters import ModelsModelsFilters
        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        page = self.page

        page_size = self.page_size

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



        total_pages = self.total_pages

        total_rows = self.total_rows


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if filters is not UNSET:
            field_dict["filters"] = filters
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if rows is not UNSET:
            field_dict["rows"] = rows
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages
        if total_rows is not UNSET:
            field_dict["total_rows"] = total_rows

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.models_model_list_item import ModelsModelListItem
        from ..models.models_models_filters import ModelsModelsFilters
        d = dict(src_dict)
        _filters = d.pop("filters", UNSET)
        filters: ModelsModelsFilters | Unset
        if isinstance(_filters,  Unset):
            filters = UNSET
        else:
            filters = ModelsModelsFilters.from_dict(_filters)




        page = d.pop("page", UNSET)

        page_size = d.pop("page_size", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[ModelsModelListItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = ModelsModelListItem.from_dict(rows_item_data)



                rows.append(rows_item)


        total_pages = d.pop("total_pages", UNSET)

        total_rows = d.pop("total_rows", UNSET)

        models_models_list_response = cls(
            filters=filters,
            page=page,
            page_size=page_size,
            rows=rows,
            total_pages=total_pages,
            total_rows=total_rows,
        )


        models_models_list_response.additional_properties = d
        return models_models_list_response

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
