from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.row_result import RowResult


T = TypeVar("T", bound="SheetResponse")


@_attrs_define
class SheetResponse:
    """Response structure for the sheet endpoint.

    Attributes:
        schema (str): The canonical specifier for the schema used in this response.
        rows (List['RowResult']): Array of rows retrieved by the query.
    """

    schema: str
    rows: List["RowResult"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schema = self.schema

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema": schema,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.row_result import RowResult

        d = src_dict.copy()
        schema = d.pop("schema")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = RowResult.from_dict(rows_item_data)

            rows.append(rows_item)

        sheet_response = cls(
            schema=schema,
            rows=rows,
        )

        sheet_response.additional_properties = d
        return sheet_response

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
