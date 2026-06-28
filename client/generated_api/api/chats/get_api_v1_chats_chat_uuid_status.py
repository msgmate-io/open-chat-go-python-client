from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chats_interaction_status_response import ChatsInteractionStatusResponse
from typing import cast



def _get_kwargs(
    chat_uuid: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/chats/{chat_uuid}/status".format(chat_uuid=quote(str(chat_uuid), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ChatsInteractionStatusResponse | str | None:
    if response.status_code == 200:
        response_200 = ChatsInteractionStatusResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ChatsInteractionStatusResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient,

) -> Response[ChatsInteractionStatusResponse | str]:
    """ Get interaction status

     Retrieve deterministic active/finished status for an interaction chat

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatsInteractionStatusResponse | str]
     """


    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    chat_uuid: str,
    *,
    client: AuthenticatedClient,

) -> ChatsInteractionStatusResponse | str | None:
    """ Get interaction status

     Retrieve deterministic active/finished status for an interaction chat

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatsInteractionStatusResponse | str
     """


    return sync_detailed(
        chat_uuid=chat_uuid,
client=client,

    ).parsed

async def asyncio_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient,

) -> Response[ChatsInteractionStatusResponse | str]:
    """ Get interaction status

     Retrieve deterministic active/finished status for an interaction chat

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ChatsInteractionStatusResponse | str]
     """


    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    chat_uuid: str,
    *,
    client: AuthenticatedClient,

) -> ChatsInteractionStatusResponse | str | None:
    """ Get interaction status

     Retrieve deterministic active/finished status for an interaction chat

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ChatsInteractionStatusResponse | str
     """


    return (await asyncio_detailed(
        chat_uuid=chat_uuid,
client=client,

    )).parsed
