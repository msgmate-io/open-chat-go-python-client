from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.tools_mcp_response import ToolsMCPResponse
from typing import cast



def _get_kwargs(
    chat_uuid: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/interactions/{chat_uuid}/mcp".format(chat_uuid=quote(str(chat_uuid), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ToolsMCPResponse | str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = ToolsMCPResponse.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ToolsMCPResponse.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ToolsMCPResponse.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ToolsMCPResponse | str]:
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

) -> Response[ToolsMCPResponse | str]:
    """ Handle MCP JSON-RPC streaming requests

     Handle Model Context Protocol streaming JSON-RPC requests for tool discovery and execution (bot
    users only)

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolsMCPResponse | str]
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

) -> ToolsMCPResponse | str | None:
    """ Handle MCP JSON-RPC streaming requests

     Handle Model Context Protocol streaming JSON-RPC requests for tool discovery and execution (bot
    users only)

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolsMCPResponse | str
     """


    return sync_detailed(
        chat_uuid=chat_uuid,
client=client,

    ).parsed

async def asyncio_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ToolsMCPResponse | str]:
    """ Handle MCP JSON-RPC streaming requests

     Handle Model Context Protocol streaming JSON-RPC requests for tool discovery and execution (bot
    users only)

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolsMCPResponse | str]
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

) -> ToolsMCPResponse | str | None:
    """ Handle MCP JSON-RPC streaming requests

     Handle Model Context Protocol streaming JSON-RPC requests for tool discovery and execution (bot
    users only)

    Args:
        chat_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolsMCPResponse | str
     """


    return (await asyncio_detailed(
        chat_uuid=chat_uuid,
client=client,

    )).parsed
