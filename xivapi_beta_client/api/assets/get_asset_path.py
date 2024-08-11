from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.format_ import Format
from ...types import UNSET, Response, Unset


def _get_kwargs(
    path: str,
    *,
    version: Union[None, Unset, str] = UNSET,
    format_: Format,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_version: Union[None, Unset, str]
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    json_format_ = format_.value
    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/asset/{path}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NOT_MODIFIED:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
    format_: Format,
) -> Response[Any]:
    """read an asset

     Read an asset from the game at the specified path, converting it into a usable format. If no valid
    conversion between the game file type and specified format exists, an error will be returned.

    Args:
        path (str): Game path of the asset to retrieve.
        version (Union[None, Unset, str]): Game version to utilise for this query.
        format_ (Format):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        path=path,
        version=version,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    path: str,
    *,
    client: Union[AuthenticatedClient, Client],
    version: Union[None, Unset, str] = UNSET,
    format_: Format,
) -> Response[Any]:
    """read an asset

     Read an asset from the game at the specified path, converting it into a usable format. If no valid
    conversion between the game file type and specified format exists, an error will be returned.

    Args:
        path (str): Game path of the asset to retrieve.
        version (Union[None, Unset, str]): Game version to utilise for this query.
        format_ (Format):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        path=path,
        version=version,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
