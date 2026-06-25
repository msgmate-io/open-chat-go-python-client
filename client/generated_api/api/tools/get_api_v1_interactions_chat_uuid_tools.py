from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_api_v1_interactions_chat_uuid_tools_response_200 import GetApiV1InteractionsChatUuidToolsResponse200
from ...models.get_api_v1_interactions_chat_uuid_tools_response_400 import GetApiV1InteractionsChatUuidToolsResponse400
from ...models.get_api_v1_interactions_chat_uuid_tools_response_403 import GetApiV1InteractionsChatUuidToolsResponse403
from ...models.get_api_v1_interactions_chat_uuid_tools_response_404 import GetApiV1InteractionsChatUuidToolsResponse404
from typing import cast



def _get_kwargs(
    chat_uuid: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/interactions/{chat_uuid}/tools".format(chat_uuid=quote(str(chat_uuid), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404 | None:
    if response.status_code == 200:
        response_200 = GetApiV1InteractionsChatUuidToolsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetApiV1InteractionsChatUuidToolsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = GetApiV1InteractionsChatUuidToolsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetApiV1InteractionsChatUuidToolsResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404]:
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

) -> Response[GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404]:
    """ Get available tools

     Get the list of available tools for a specific chat (bot users only)

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404]
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
    client: AuthenticatedClient | Client,

) -> GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404 | None:
    """ Get available tools

     Get the list of available tools for a specific chat (bot users only)

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404
     """


    return sync_detailed(
        chat_uuid=chat_uuid,
client=client,

    ).parsed

async def asyncio_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404]:
    """ Get available tools

     Get the list of available tools for a specific chat (bot users only)

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404]
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
    client: AuthenticatedClient | Client,

) -> GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404 | None:
    """ Get available tools

     Get the list of available tools for a specific chat (bot users only)

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetApiV1InteractionsChatUuidToolsResponse200 | GetApiV1InteractionsChatUuidToolsResponse400 | GetApiV1InteractionsChatUuidToolsResponse403 | GetApiV1InteractionsChatUuidToolsResponse404
     """


    return (await asyncio_detailed(
        chat_uuid=chat_uuid,
client=client,

    )).parsed
