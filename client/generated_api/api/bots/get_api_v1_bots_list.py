from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bots_listed_bots_page import BotsListedBotsPage
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    include_public: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["include_public"] = include_public


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/bots/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BotsListedBotsPage | None:
    if response.status_code == 200:
        response_200 = BotsListedBotsPage.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BotsListedBotsPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    include_public: bool | Unset = UNSET,

) -> Response[BotsListedBotsPage]:
    """ List bots

     List owner bots, optionally including public bots from other owners

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.
        include_public (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotsListedBotsPage]
     """


    kwargs = _get_kwargs(
        page=page,
limit=limit,
include_public=include_public,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    include_public: bool | Unset = UNSET,

) -> BotsListedBotsPage | None:
    """ List bots

     List owner bots, optionally including public bots from other owners

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.
        include_public (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotsListedBotsPage
     """


    return sync_detailed(
        client=client,
page=page,
limit=limit,
include_public=include_public,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    include_public: bool | Unset = UNSET,

) -> Response[BotsListedBotsPage]:
    """ List bots

     List owner bots, optionally including public bots from other owners

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.
        include_public (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotsListedBotsPage]
     """


    kwargs = _get_kwargs(
        page=page,
limit=limit,
include_public=include_public,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    include_public: bool | Unset = UNSET,

) -> BotsListedBotsPage | None:
    """ List bots

     List owner bots, optionally including public bots from other owners

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.
        include_public (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotsListedBotsPage
     """


    return (await asyncio_detailed(
        client=client,
page=page,
limit=limit,
include_public=include_public,

    )).parsed
