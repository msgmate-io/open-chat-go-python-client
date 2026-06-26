from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_api_v1_tools_typing_tool_name_call_validate_body import PostApiV1ToolsTypingToolNameCallValidateBody
from ...models.tools_tool_validate_payload_response import ToolsToolValidatePayloadResponse
from typing import cast



def _get_kwargs(
    tool_name: str,
    *,
    body: PostApiV1ToolsTypingToolNameCallValidateBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tools/typing/{tool_name}/call/validate".format(tool_name=quote(str(tool_name), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ToolsToolValidatePayloadResponse | str | None:
    if response.status_code == 200:
        response_200 = ToolsToolValidatePayloadResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ToolsToolValidatePayloadResponse | str]:
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
    body: PostApiV1ToolsTypingToolNameCallValidateBody,

) -> Response[ToolsToolValidatePayloadResponse | str]:
    """ Validate tool call payload

     Validate a JSON object payload for a tool call by tool name.

    Args:
        tool_name (str):
        body (PostApiV1ToolsTypingToolNameCallValidateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolsToolValidatePayloadResponse | str]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1ToolsTypingToolNameCallValidateBody,

) -> ToolsToolValidatePayloadResponse | str | None:
    """ Validate tool call payload

     Validate a JSON object payload for a tool call by tool name.

    Args:
        tool_name (str):
        body (PostApiV1ToolsTypingToolNameCallValidateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolsToolValidatePayloadResponse | str
     """


    return sync_detailed(
        tool_name=tool_name,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1ToolsTypingToolNameCallValidateBody,

) -> Response[ToolsToolValidatePayloadResponse | str]:
    """ Validate tool call payload

     Validate a JSON object payload for a tool call by tool name.

    Args:
        tool_name (str):
        body (PostApiV1ToolsTypingToolNameCallValidateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ToolsToolValidatePayloadResponse | str]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tool_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1ToolsTypingToolNameCallValidateBody,

) -> ToolsToolValidatePayloadResponse | str | None:
    """ Validate tool call payload

     Validate a JSON object payload for a tool call by tool name.

    Args:
        tool_name (str):
        body (PostApiV1ToolsTypingToolNameCallValidateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ToolsToolValidatePayloadResponse | str
     """


    return (await asyncio_detailed(
        tool_name=tool_name,
client=client,
body=body,

    )).parsed
