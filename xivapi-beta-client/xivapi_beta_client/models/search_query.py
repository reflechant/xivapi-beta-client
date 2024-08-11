from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchQuery")


@_attrs_define
class SearchQuery:
    """Query paramters accepted by the search endpoint.

    Attributes:
        query (Union[None, Unset, str]): Search query to execute in this request. Must be specified if not querying a
            cursor. URL special characters, such as `+`, must be escaped to prevent mis-parses of the query.
        sheets (Union[None, Unset, str]): List of excel sheets that the query should be run against. At least one must
            be specified if not querying a cursor.
        cursor (Union[None, Unset, str]): Continuation token to retrieve further results from a prior search request. If
            specified, takes priority over `query`.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide the cursor token
            provided in `next` to the `cursor` paramter.
    """

    query: Union[None, Unset, str] = UNSET
    sheets: Union[None, Unset, str] = UNSET
    cursor: Union[None, Unset, str] = UNSET
    limit: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query: Union[None, Unset, str]
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        sheets: Union[None, Unset, str]
        if isinstance(self.sheets, Unset):
            sheets = UNSET
        else:
            sheets = self.sheets

        cursor: Union[None, Unset, str]
        if isinstance(self.cursor, Unset):
            cursor = UNSET
        else:
            cursor = self.cursor

        limit: Union[None, Unset, int]
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if sheets is not UNSET:
            field_dict["sheets"] = sheets
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_query(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_sheets(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sheets = _parse_sheets(d.pop("sheets", UNSET))

        def _parse_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cursor = _parse_cursor(d.pop("cursor", UNSET))

        def _parse_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limit = _parse_limit(d.pop("limit", UNSET))

        search_query = cls(
            query=query,
            sheets=sheets,
            cursor=cursor,
            limit=limit,
        )

        search_query.additional_properties = d
        return search_query

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
