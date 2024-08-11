from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.language_string import LanguageString
from ...models.sheet_response import SheetResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    sheet: str,
    *,
    rows: Union[Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    after: Union[None, Unset, str] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["rows"] = rows

    json_limit: Union[None, Unset, int]
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_after: Union[None, Unset, str]
    if isinstance(after, Unset):
        json_after = UNSET
    else:
        json_after = after
    params["after"] = json_after

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
        "url": f"/sheet/{sheet}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[SheetResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SheetResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[SheetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    sheet: str,
    *,
    client: Union[AuthenticatedClient, Client],
    rows: Union[Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    after: Union[None, Unset, str] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Response[SheetResponse]:
    """list rows in a sheet

     Read information about one or more rows and their related data.

    Args:
        sheet (str): Name of the sheet to read.
        rows (Union[Unset, str]): Rows to fetch from the sheet, as a comma-separated list.
            Behavior is undefined if both `rows` and `after` are provided.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide
            the last returned row to the next request's `after` parameter.
        after (Union[None, Unset, str]): Fetch rows after the specified row. Behavior is undefined
            if both `rows` and `after` are provided.
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
        Response[SheetResponse]
    """

    kwargs = _get_kwargs(
        sheet=sheet,
        rows=rows,
        limit=limit,
        after=after,
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
    *,
    client: Union[AuthenticatedClient, Client],
    rows: Union[Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    after: Union[None, Unset, str] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Optional[SheetResponse]:
    """list rows in a sheet

     Read information about one or more rows and their related data.

    Args:
        sheet (str): Name of the sheet to read.
        rows (Union[Unset, str]): Rows to fetch from the sheet, as a comma-separated list.
            Behavior is undefined if both `rows` and `after` are provided.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide
            the last returned row to the next request's `after` parameter.
        after (Union[None, Unset, str]): Fetch rows after the specified row. Behavior is undefined
            if both `rows` and `after` are provided.
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
        SheetResponse
    """

    return sync_detailed(
        sheet=sheet,
        client=client,
        rows=rows,
        limit=limit,
        after=after,
        language=language,
        schema=schema,
        fields=fields,
        transient=transient,
    ).parsed


async def asyncio_detailed(
    sheet: str,
    *,
    client: Union[AuthenticatedClient, Client],
    rows: Union[Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    after: Union[None, Unset, str] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Response[SheetResponse]:
    """list rows in a sheet

     Read information about one or more rows and their related data.

    Args:
        sheet (str): Name of the sheet to read.
        rows (Union[Unset, str]): Rows to fetch from the sheet, as a comma-separated list.
            Behavior is undefined if both `rows` and `after` are provided.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide
            the last returned row to the next request's `after` parameter.
        after (Union[None, Unset, str]): Fetch rows after the specified row. Behavior is undefined
            if both `rows` and `after` are provided.
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
        Response[SheetResponse]
    """

    kwargs = _get_kwargs(
        sheet=sheet,
        rows=rows,
        limit=limit,
        after=after,
        language=language,
        schema=schema,
        fields=fields,
        transient=transient,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    sheet: str,
    *,
    client: Union[AuthenticatedClient, Client],
    rows: Union[Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    after: Union[None, Unset, str] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Optional[SheetResponse]:
    """list rows in a sheet

     Read information about one or more rows and their related data.

    Args:
        sheet (str): Name of the sheet to read.
        rows (Union[Unset, str]): Rows to fetch from the sheet, as a comma-separated list.
            Behavior is undefined if both `rows` and `after` are provided.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide
            the last returned row to the next request's `after` parameter.
        after (Union[None, Unset, str]): Fetch rows after the specified row. Behavior is undefined
            if both `rows` and `after` are provided.
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
        SheetResponse
    """

    return (
        await asyncio_detailed(
            sheet=sheet,
            client=client,
            rows=rows,
            limit=limit,
            after=after,
            language=language,
            schema=schema,
            fields=fields,
            transient=transient,
        )
    ).parsed
