from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.tools_tool_type_definition import ToolsToolTypeDefinition
from typing import cast



def _get_kwargs(
    tool_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/tools/{tool_name}/typing".format(tool_name=quote(str(tool_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ToolsToolTypeDefinition | str | None:
    if response.status_code == 200:
        response_200 = ToolsToolTypeDefinition.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ToolsToolTypeDefinition | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ToolsToolTypeDefinition | str]:
    """ Get tool typing schema

     Get a single visible tool typing schema by tool name.

    Args:
        tool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolsToolTypeDefinition | str]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> ToolsToolTypeDefinition | str | None:
    """ Get tool typing schema

     Get a single visible tool typing schema by tool name.

    Args:
        tool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolsToolTypeDefinition | str
     """


    return sync_detailed(
        tool_name=tool_name,
client=client,

    ).parsed

async def asyncio_detailed(
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ToolsToolTypeDefinition | str]:
    """ Get tool typing schema

     Get a single visible tool typing schema by tool name.

    Args:
        tool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolsToolTypeDefinition | str]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> ToolsToolTypeDefinition | str | None:
    """ Get tool typing schema

     Get a single visible tool typing schema by tool name.

    Args:
        tool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolsToolTypeDefinition | str
     """


    return (await asyncio_detailed(
        tool_name=tool_name,
client=client,

    )).parsed
