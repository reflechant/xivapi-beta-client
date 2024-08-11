from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.language_string import LanguageString
from ...models.search_response import SearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    version: Union[None, Unset, str] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    sheets: Union[None, Unset, str] = UNSET,
    cursor: Union[None, Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_version: Union[None, Unset, str]
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    json_query: Union[None, Unset, str]
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_sheets: Union[None, Unset, str]
    if isinstance(sheets, Unset):
        json_sheets = UNSET
    else:
        json_sheets = sheets
    params["sheets"] = json_sheets

    json_cursor: Union[None, Unset, str]
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_limit: Union[None, Unset, int]
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

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
        "url": "/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SearchResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SearchResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    sheets: Union[None, Unset, str] = UNSET,
    cursor: Union[None, Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Response[SearchResponse]:
    """execute a search query

     Fetch information about rows and their related data that match the provided search query.

    Args:
        version (Union[None, Unset, str]): Game version to utilise for this query.
        query (Union[None, Unset, str]): Search query to execute in this request. Must be
            specified if not querying a cursor. URL special characters, such as `+`, must be escaped
            to prevent mis-parses of the query.
        sheets (Union[None, Unset, str]): List of excel sheets that the query should be run
            against. At least one must be specified if not querying a cursor.
        cursor (Union[None, Unset, str]): Continuation token to retrieve further results from a
            prior search request. If specified, takes priority over `query`.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide
            the cursor token provided in `next` to the `cursor` paramter.
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
        Response[SearchResponse]
    """

    kwargs = _get_kwargs(
        version=version,
        query=query,
        sheets=sheets,
        cursor=cursor,
        limit=limit,
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
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    sheets: Union[None, Unset, str] = UNSET,
    cursor: Union[None, Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Optional[SearchResponse]:
    """execute a search query

     Fetch information about rows and their related data that match the provided search query.

    Args:
        version (Union[None, Unset, str]): Game version to utilise for this query.
        query (Union[None, Unset, str]): Search query to execute in this request. Must be
            specified if not querying a cursor. URL special characters, such as `+`, must be escaped
            to prevent mis-parses of the query.
        sheets (Union[None, Unset, str]): List of excel sheets that the query should be run
            against. At least one must be specified if not querying a cursor.
        cursor (Union[None, Unset, str]): Continuation token to retrieve further results from a
            prior search request. If specified, takes priority over `query`.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide
            the cursor token provided in `next` to the `cursor` paramter.
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
        SearchResponse
    """

    return sync_detailed(
        client=client,
        version=version,
        query=query,
        sheets=sheets,
        cursor=cursor,
        limit=limit,
        language=language,
        schema=schema,
        fields=fields,
        transient=transient,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    sheets: Union[None, Unset, str] = UNSET,
    cursor: Union[None, Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Response[SearchResponse]:
    """execute a search query

     Fetch information about rows and their related data that match the provided search query.

    Args:
        version (Union[None, Unset, str]): Game version to utilise for this query.
        query (Union[None, Unset, str]): Search query to execute in this request. Must be
            specified if not querying a cursor. URL special characters, such as `+`, must be escaped
            to prevent mis-parses of the query.
        sheets (Union[None, Unset, str]): List of excel sheets that the query should be run
            against. At least one must be specified if not querying a cursor.
        cursor (Union[None, Unset, str]): Continuation token to retrieve further results from a
            prior search request. If specified, takes priority over `query`.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide
            the cursor token provided in `next` to the `cursor` paramter.
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
        Response[SearchResponse]
    """

    kwargs = _get_kwargs(
        version=version,
        query=query,
        sheets=sheets,
        cursor=cursor,
        limit=limit,
        language=language,
        schema=schema,
        fields=fields,
        transient=transient,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
    query: Union[None, Unset, str] = UNSET,
    sheets: Union[None, Unset, str] = UNSET,
    cursor: Union[None, Unset, str] = UNSET,
    limit: Union[None, Unset, int] = UNSET,
    language: Union[LanguageString, None, Unset] = UNSET,
    schema: Union[None, Unset, str] = UNSET,
    fields: Union[None, Unset, str] = UNSET,
    transient: Union[None, Unset, str] = UNSET,
) -> Optional[SearchResponse]:
    """execute a search query

     Fetch information about rows and their related data that match the provided search query.

    Args:
        version (Union[None, Unset, str]): Game version to utilise for this query.
        query (Union[None, Unset, str]): Search query to execute in this request. Must be
            specified if not querying a cursor. URL special characters, such as `+`, must be escaped
            to prevent mis-parses of the query.
        sheets (Union[None, Unset, str]): List of excel sheets that the query should be run
            against. At least one must be specified if not querying a cursor.
        cursor (Union[None, Unset, str]): Continuation token to retrieve further results from a
            prior search request. If specified, takes priority over `query`.
        limit (Union[None, Unset, int]): Maximum number of rows to return. To paginate, provide
            the cursor token provided in `next` to the `cursor` paramter.
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
        SearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            version=version,
            query=query,
            sheets=sheets,
            cursor=cursor,
            limit=limit,
            language=language,
            schema=schema,
            fields=fields,
            transient=transient,
        )
    ).parsed
