from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    version: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_version: Union[None, Unset, str]
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/sheet",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[List[str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(List[str], response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[List[str]]:
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
) -> Response[List[str]]:
    """list sheets

     List known excel sheet names that can be read by the API.

    Args:
        version (Union[None, Unset, str]): Game version to utilise for this query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
) -> Optional[List[str]]:
    """list sheets

     List known excel sheet names that can be read by the API.

    Args:
        version (Union[None, Unset, str]): Game version to utilise for this query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return sync_detailed(
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
) -> Response[List[str]]:
    """list sheets

     List known excel sheet names that can be read by the API.

    Args:
        version (Union[None, Unset, str]): Game version to utilise for this query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List[str]]
    """

    kwargs = _get_kwargs(
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
) -> Optional[List[str]]:
    """list sheets

     List known excel sheet names that can be read by the API.

    Args:
        version (Union[None, Unset, str]): Game version to utilise for this query.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List[str]
    """

    return (
        await asyncio_detailed(
            client=client,
            version=version,
        )
    ).parsed
