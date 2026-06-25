from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chats_listed_message import ChatsListedMessage





T = TypeVar("T", bound="ChatsListedMessagesPage")



@_attrs_define
class ChatsListedMessagesPage:
    """ 
        Attributes:
            limit (int | Unset):
            page (int | Unset):
            rows (list[ChatsListedMessage] | Unset):
            total_pages (int | Unset):
     """

    limit: int | Unset = UNSET
    page: int | Unset = UNSET
    rows: list[ChatsListedMessage] | Unset = UNSET
    total_pages: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chats_listed_message import ChatsListedMessage
        limit = self.limit

        page = self.page

        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



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
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chats_listed_message import ChatsListedMessage
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        page = d.pop("page", UNSET)

        _rows = d.pop("rows", UNSET)
        rows: list[ChatsListedMessage] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = ChatsListedMessage.from_dict(rows_item_data)



                rows.append(rows_item)


        total_pages = d.pop("total_pages", UNSET)

        chats_listed_messages_page = cls(
            limit=limit,
            page=page,
            rows=rows,
            total_pages=total_pages,
        )


        chats_listed_messages_page.additional_properties = d
        return chats_listed_messages_page

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
