from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.value_string import ValueString


T = TypeVar("T", bound="RowResult")


@_attrs_define
class RowResult:
    """
    Attributes:
        row_id (int): ID of this row.
        fields (ValueString):
        subrow_id (Union[None, Unset, int]): Subrow ID of this row, when relevant.
        transient (Union['ValueString', None, Unset]): Field values for this row's transient row, if any is present,
            according to the current schema and transient filter.
    """

    row_id: int
    fields: "ValueString"
    subrow_id: Union[None, Unset, int] = UNSET
    transient: Union["ValueString", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.value_string import ValueString

        row_id = self.row_id

        fields = self.fields.to_dict()

        subrow_id: Union[None, Unset, int]
        if isinstance(self.subrow_id, Unset):
            subrow_id = UNSET
        else:
            subrow_id = self.subrow_id

        transient: Union[Dict[str, Any], None, Unset]
        if isinstance(self.transient, Unset):
            transient = UNSET
        elif isinstance(self.transient, ValueString):
            transient = self.transient.to_dict()
        else:
            transient = self.transient

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "row_id": row_id,
                "fields": fields,
            }
        )
        if subrow_id is not UNSET:
            field_dict["subrow_id"] = subrow_id
        if transient is not UNSET:
            field_dict["transient"] = transient

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.value_string import ValueString

        d = src_dict.copy()
        row_id = d.pop("row_id")

        fields = ValueString.from_dict(d.pop("fields"))

        def _parse_subrow_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        subrow_id = _parse_subrow_id(d.pop("subrow_id", UNSET))

        def _parse_transient(data: object) -> Union["ValueString", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transient_type_0 = ValueString.from_dict(data)

                return transient_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ValueString", None, Unset], data)

        transient = _parse_transient(d.pop("transient", UNSET))

        row_result = cls(
            row_id=row_id,
            fields=fields,
            subrow_id=subrow_id,
            transient=transient,
        )

        row_result.additional_properties = d
        return row_result

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
