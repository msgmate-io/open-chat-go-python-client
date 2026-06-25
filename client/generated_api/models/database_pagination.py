from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DatabasePagination")



@_attrs_define
class DatabasePagination:
    """ 
        Attributes:
            limit (int | Unset):
            page (int | Unset):
            rows (Any | Unset):
            sort (str | Unset):
            total_pages (int | Unset):
     """

    limit: int | Unset = UNSET
    page: int | Unset = UNSET
    rows: Any | Unset = UNSET
    sort: str | Unset = UNSET
    total_pages: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        page = self.page

        rows = self.rows

        sort = self.sort

        total_pages = self.total_pages


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if limit is not UNSET:
            field_dict["limit"] = limit
        if page is not UNSET:
            field_dict["page"] = page
        if rows is not UNSET:
            field_dict["rows"] = rows
        if sort is not UNSET:
            field_dict["sort"] = sort
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        page = d.pop("page", UNSET)

        rows = d.pop("rows", UNSET)

        sort = d.pop("sort", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        database_pagination = cls(
            limit=limit,
            page=page,
            rows=rows,
            sort=sort,
            total_pages=total_pages,
        )


        database_pagination.additional_properties = d
        return database_pagination

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
