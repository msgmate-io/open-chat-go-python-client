from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.tools_tools_list_response import ToolsToolsListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    type_: str | Unset = UNSET,
    q: str | Unset = UNSET,
    requires_init: str | Unset = UNSET,
    requires_confirmation: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["type"] = type_

    params["q"] = q

    params["requires_init"] = requires_init

    params["requires_confirmation"] = requires_confirmation


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tools/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ToolsToolsListResponse | None:
    if response.status_code == 200:
        response_200 = ToolsToolsListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ToolsToolsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    type_: str | Unset = UNSET,
    q: str | Unset = UNSET,
    requires_init: str | Unset = UNSET,
    requires_confirmation: str | Unset = UNSET,

) -> Response[ToolsToolsListResponse]:
    """ List tools

     List callable tools with pagination and filters. Admin-only tools are only visible to admin users.

    Args:
        page (int | Unset):
        page_size (int | Unset):
        type_ (str | Unset):
        q (str | Unset):
        requires_init (str | Unset):
        requires_confirmation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolsToolsListResponse]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
type_=type_,
q=q,
requires_init=requires_init,
requires_confirmation=requires_confirmation,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    type_: str | Unset = UNSET,
    q: str | Unset = UNSET,
    requires_init: str | Unset = UNSET,
    requires_confirmation: str | Unset = UNSET,

) -> ToolsToolsListResponse | None:
    """ List tools

     List callable tools with pagination and filters. Admin-only tools are only visible to admin users.

    Args:
        page (int | Unset):
        page_size (int | Unset):
        type_ (str | Unset):
        q (str | Unset):
        requires_init (str | Unset):
        requires_confirmation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolsToolsListResponse
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
type_=type_,
q=q,
requires_init=requires_init,
requires_confirmation=requires_confirmation,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    type_: str | Unset = UNSET,
    q: str | Unset = UNSET,
    requires_init: str | Unset = UNSET,
    requires_confirmation: str | Unset = UNSET,

) -> Response[ToolsToolsListResponse]:
    """ List tools

     List callable tools with pagination and filters. Admin-only tools are only visible to admin users.

    Args:
        page (int | Unset):
        page_size (int | Unset):
        type_ (str | Unset):
        q (str | Unset):
        requires_init (str | Unset):
        requires_confirmation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolsToolsListResponse]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
type_=type_,
q=q,
requires_init=requires_init,
requires_confirmation=requires_confirmation,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    type_: str | Unset = UNSET,
    q: str | Unset = UNSET,
    requires_init: str | Unset = UNSET,
    requires_confirmation: str | Unset = UNSET,

) -> ToolsToolsListResponse | None:
    """ List tools

     List callable tools with pagination and filters. Admin-only tools are only visible to admin users.

    Args:
        page (int | Unset):
        page_size (int | Unset):
        type_ (str | Unset):
        q (str | Unset):
        requires_init (str | Unset):
        requires_confirmation (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolsToolsListResponse
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
type_=type_,
q=q,
requires_init=requires_init,
requires_confirmation=requires_confirmation,

    )).parsed
