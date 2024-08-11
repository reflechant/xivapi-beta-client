from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.language_string import LanguageString
from ...models.row_response import RowResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sheet: str,
    row: str,
    *,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_language: Union[None, Unset, str]
    if isinstance(language, Unset):
        json_language = UNSET
    elif isinstance(language, LanguageString):
        json_language = language.value
    else:
        json_language = language
    params["language"] = json_language

    json_schema: Union[None, Unset, str]
    if isinstance(schema, Unset):
        json_schema = UNSET
    else:
        json_schema = schema
    params["schema"] = json_schema

    json_fields: Union[None, Unset, str]
    if isinstance(fields, Unset):
        json_fields = UNSET
    else:
        json_fields = fields
    params["fields"] = json_fields

    json_transient: Union[None, Unset, str]
    if isinstance(transient, Unset):
        json_transient = UNSET
    else:
        json_transient = transient
    params["transient"] = json_transient

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/sheet/{sheet}/{row}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[RowResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RowResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[RowResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sheet: str,
    row: str,
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Response[RowResponse]:
    """read a sheet row

     Read detailed, filterable information from a single sheet row and its related data.

    Args:
        sheet (str): Name of the sheet to read.
        row (str):
        language (Union[LanguageString, None, Unset]): Language to use for data with no language
            otherwise specified in the fields filter.
        schema (Union[None, Unset, str]): Schema that row data should be read with.
        fields (Union[None, Unset, str]): Data fields to read for selected rows.
        transient (Union[None, Unset, str]): Data fields to read for selected rows' transient row,
            if any is present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RowResponse]
    """

    kwargs = _get_kwargs(
        sheet=sheet,
        row=row,
        language=language,
        schema=schema,
        fields=fields,
        transient=transient,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    sheet: str,
    row: str,
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Optional[RowResponse]:
    """read a sheet row

     Read detailed, filterable information from a single sheet row and its related data.

    Args:
        sheet (str): Name of the sheet to read.
        row (str):
        language (Union[LanguageString, None, Unset]): Language to use for data with no language
            otherwise specified in the fields filter.
        schema (Union[None, Unset, str]): Schema that row data should be read with.
        fields (Union[None, Unset, str]): Data fields to read for selected rows.
        transient (Union[None, Unset, str]): Data fields to read for selected rows' transient row,
            if any is present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RowResponse
    """

    return sync_detailed(
        sheet=sheet,
        row=row,
        client=client,
        language=language,
        schema=schema,
        fields=fields,
        transient=transient,
    ).parsed


async def asyncio_detailed(
    sheet: str,
    row: str,
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Response[RowResponse]:
    """read a sheet row

     Read detailed, filterable information from a single sheet row and its related data.

    Args:
        sheet (str): Name of the sheet to read.
        row (str):
        language (Union[LanguageString, None, Unset]): Language to use for data with no language
            otherwise specified in the fields filter.
        schema (Union[None, Unset, str]): Schema that row data should be read with.
        fields (Union[None, Unset, str]): Data fields to read for selected rows.
        transient (Union[None, Unset, str]): Data fields to read for selected rows' transient row,
            if any is present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RowResponse]
    """

    kwargs = _get_kwargs(
        sheet=sheet,
        row=row,
        language=language,
        schema=schema,
        fields=fields,
        transient=transient,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sheet: str,
    row: str,
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Optional[RowResponse]:
    """read a sheet row

     Read detailed, filterable information from a single sheet row and its related data.

    Args:
        sheet (str): Name of the sheet to read.
        row (str):
        language (Union[LanguageString, None, Unset]): Language to use for data with no language
            otherwise specified in the fields filter.
        schema (Union[None, Unset, str]): Schema that row data should be read with.
        fields (Union[None, Unset, str]): Data fields to read for selected rows.
        transient (Union[None, Unset, str]): Data fields to read for selected rows' transient row,
            if any is present.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RowResponse
    """

    return (
        await asyncio_detailed(
            sheet=sheet,
            row=row,
            client=client,
            language=language,
            schema=schema,
            fields=fields,
            transient=transient,
        )
    ).parsed
