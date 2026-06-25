from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chats_listed_chats_page import ChatsListedChatsPage
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    chat_types: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params["chat_types"] = chat_types


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/chats/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatsListedChatsPage | str | None:
    if response.status_code == 200:
        response_200 = ChatsListedChatsPage.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatsListedChatsPage | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    chat_types: str | Unset = UNSET,

) -> Response[ChatsListedChatsPage | str]:
    """ Get user chats

     Retrieve a list of chats for the authenticated user

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.
        chat_types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatsListedChatsPage | str]
     """


    kwargs = _get_kwargs(
        page=page,
limit=limit,
chat_types=chat_types,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    chat_types: str | Unset = UNSET,

) -> ChatsListedChatsPage | str | None:
    """ Get user chats

     Retrieve a list of chats for the authenticated user

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.
        chat_types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatsListedChatsPage | str
     """


    return sync_detailed(
        client=client,
page=page,
limit=limit,
chat_types=chat_types,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    chat_types: str | Unset = UNSET,

) -> Response[ChatsListedChatsPage | str]:
    """ Get user chats

     Retrieve a list of chats for the authenticated user

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.
        chat_types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatsListedChatsPage | str]
     """


    kwargs = _get_kwargs(
        page=page,
limit=limit,
chat_types=chat_types,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 40,
    chat_types: str | Unset = UNSET,

) -> ChatsListedChatsPage | str | None:
    """ Get user chats

     Retrieve a list of chats for the authenticated user

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.
        chat_types (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatsListedChatsPage | str
     """


    return (await asyncio_detailed(
        client=client,
page=page,
limit=limit,
chat_types=chat_types,

    )).parsed
