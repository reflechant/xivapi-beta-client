from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SheetQuery")


@_attrs_define
class SheetQuery:
    """Query parameters accepted by the sheet endpoint.

    Attributes:
        rows (Union[Unset, str]): Rows to fetch from the sheet, as a comma-separated list. Behavior is undefined if both
            `rows` and `after` are provided.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide the last returned row to
            the next request's `after` parameter.
        after (Union[None, Unset, str]): Fetch rows after the specified row. Behavior is undefined if both `rows` and
            `after` are provided.
    """

    rows: Union[Unset, str] = UNSET
    limit: Union[None, Unset, int] = UNSET
    after: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rows = self.rows

        limit: Union[None, Unset, int]
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        after: Union[None, Unset, str]
        if isinstance(self.after, Unset):
            after = UNSET
        else:
            after = self.after

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rows is not UNSET:
            field_dict["rows"] = rows
        if limit is not UNSET:
            field_dict["limit"] = limit
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rows = d.pop("rows", UNSET)

        def _parse_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_after(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        after = _parse_after(d.pop("after", UNSET))

        sheet_query = cls(
            rows=rows,
            limit=limit,
            after=after,
        )

        sheet_query.additional_properties = d
        return sheet_query

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
