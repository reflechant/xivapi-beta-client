from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RowPath")


@_attrs_define
class RowPath:
    """Path variables accepted by the row endpoint.

    Attributes:
        sheet (str): Name of the sheet to read.
        row (str):
    """

    sheet: str
    row: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sheet = self.sheet

        row = self.row

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sheet": sheet,
                "row": row,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sheet = d.pop("sheet")

        row = d.pop("row")

        row_path = cls(
            sheet=sheet,
            row=row,
        )

        row_path.additional_properties = d
        return row_path

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
