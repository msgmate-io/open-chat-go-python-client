from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_api_v1_interactions_chat_uuid_tools_tool_name_response_400 import PostApiV1InteractionsChatUuidToolsToolNameResponse400
from ...models.post_api_v1_interactions_chat_uuid_tools_tool_name_response_403 import PostApiV1InteractionsChatUuidToolsToolNameResponse403
from ...models.post_api_v1_interactions_chat_uuid_tools_tool_name_response_404 import PostApiV1InteractionsChatUuidToolsToolNameResponse404
from ...models.tools_tool_execution_request import ToolsToolExecutionRequest
from ...models.tools_tool_execution_response import ToolsToolExecutionResponse
from typing import cast



def _get_kwargs(
    chat_uuid: str,
    tool_name: str,
    *,
    body: ToolsToolExecutionRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/interactions/{chat_uuid}/tools/{tool_name}".format(chat_uuid=quote(str(chat_uuid), safe=""),tool_name=quote(str(tool_name), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse | None:
    if response.status_code == 200:
        response_200 = ToolsToolExecutionResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostApiV1InteractionsChatUuidToolsToolNameResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = PostApiV1InteractionsChatUuidToolsToolNameResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostApiV1InteractionsChatUuidToolsToolNameResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_uuid: str,
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolsToolExecutionRequest,

) -> Response[PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse]:
    """ Execute a tool

     Execute a tool for a specific chat interaction (bot users only)

    Args:
        chat_uuid (str):
        tool_name (str):
        body (ToolsToolExecutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse]
     """


    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,
tool_name=tool_name,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    chat_uuid: str,
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolsToolExecutionRequest,

) -> PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse | None:
    """ Execute a tool

     Execute a tool for a specific chat interaction (bot users only)

    Args:
        chat_uuid (str):
        tool_name (str):
        body (ToolsToolExecutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse
     """


    return sync_detailed(
        chat_uuid=chat_uuid,
tool_name=tool_name,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    chat_uuid: str,
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolsToolExecutionRequest,

) -> Response[PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse]:
    """ Execute a tool

     Execute a tool for a specific chat interaction (bot users only)

    Args:
        chat_uuid (str):
        tool_name (str):
        body (ToolsToolExecutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse]
     """


    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,
tool_name=tool_name,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    chat_uuid: str,
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolsToolExecutionRequest,

) -> PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse | None:
    """ Execute a tool

     Execute a tool for a specific chat interaction (bot users only)

    Args:
        chat_uuid (str):
        tool_name (str):
        body (ToolsToolExecutionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiV1InteractionsChatUuidToolsToolNameResponse400 | PostApiV1InteractionsChatUuidToolsToolNameResponse403 | PostApiV1InteractionsChatUuidToolsToolNameResponse404 | ToolsToolExecutionResponse
     """


    return (await asyncio_detailed(
        chat_uuid=chat_uuid,
tool_name=tool_name,
client=client,
body=body,

    )).parsed
