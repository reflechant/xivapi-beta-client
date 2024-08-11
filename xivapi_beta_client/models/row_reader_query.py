from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.language_string import LanguageString
from ..types import UNSET, Unset

T = TypeVar("T", bound="RowReaderQuery")


@_attrs_define
class RowReaderQuery:
    """Query parameters accepted by endpoints that retrieve excel row data.

    Attributes:
        language (Union[LanguageString, None, Unset]): Language to use for data with no language otherwise specified in
            the fields filter.
        schema (Union[None, Unset, str]): Schema that row data should be read with.
        fields (Union[None, Unset, str]): Data fields to read for selected rows.
        transient (Union[None, Unset, str]): Data fields to read for selected rows' transient row, if any is present.
    """

    language: Union[LanguageString, None, Unset] = UNSET
    schema: Union[None, Unset, str] = UNSET
    fields: Union[None, Unset, str] = UNSET
    transient: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language: Union[None, Unset, str]
        if isinstance(self.language, Unset):
            language = UNSET
        elif isinstance(self.language, LanguageString):
            language = self.language.value
        else:
            language = self.language

        schema: Union[None, Unset, str]
        if isinstance(self.schema, Unset):
            schema = UNSET
        else:
            schema = self.schema

        fields: Union[None, Unset, str]
        if isinstance(self.fields, Unset):
            fields = UNSET
        else:
            fields = self.fields

        transient: Union[None, Unset, str]
        if isinstance(self.transient, Unset):
            transient = UNSET
        else:
            transient = self.transient

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if schema is not UNSET:
            field_dict["schema"] = schema
        if fields is not UNSET:
            field_dict["fields"] = fields
        if transient is not UNSET:
            field_dict["transient"] = transient

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_language(data: object) -> Union[LanguageString, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                language_type_0 = LanguageString(data)

                return language_type_0
            except:  # noqa: E722
                pass
            return cast(Union[LanguageString, None, Unset], data)

        language = _parse_language(d.pop("language", UNSET))

        def _parse_schema(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_fields(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_transient(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        transient = _parse_transient(d.pop("transient", UNSET))

        row_reader_query = cls(
            language=language,
            schema=schema,
            fields=fields,
            transient=transient,
        )

        row_reader_query.additional_properties = d
        return row_reader_query

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
