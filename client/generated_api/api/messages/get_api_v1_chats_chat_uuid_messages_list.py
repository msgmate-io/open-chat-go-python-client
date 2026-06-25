from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chats_listed_messages_page import ChatsListedMessagesPage
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    chat_uuid: str,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 10,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/chats/{chat_uuid}/messages/list".format(chat_uuid=quote(str(chat_uuid), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatsListedMessagesPage | str | None:
    if response.status_code == 200:
        response_200 = ChatsListedMessagesPage.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatsListedMessagesPage | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,

) -> Response[ChatsListedMessagesPage | str]:
    """ Get Chat messages

     Retrieve a list of messages associated with a specific chat UUID

    Args:
        chat_uuid (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatsListedMessagesPage | str]
     """


    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,
page=page,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,

) -> ChatsListedMessagesPage | str | None:
    """ Get Chat messages

     Retrieve a list of messages associated with a specific chat UUID

    Args:
        chat_uuid (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatsListedMessagesPage | str
     """


    return sync_detailed(
        chat_uuid=chat_uuid,
client=client,
page=page,
limit=limit,

    ).parsed

async def asyncio_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,

) -> Response[ChatsListedMessagesPage | str]:
    """ Get Chat messages

     Retrieve a list of messages associated with a specific chat UUID

    Args:
        chat_uuid (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatsListedMessagesPage | str]
     """


    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,
page=page,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 10,

) -> ChatsListedMessagesPage | str | None:
    """ Get Chat messages

     Retrieve a list of messages associated with a specific chat UUID

    Args:
        chat_uuid (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatsListedMessagesPage | str
     """


    return (await asyncio_detailed(
        chat_uuid=chat_uuid,
client=client,
page=page,
limit=limit,

    )).parsed
