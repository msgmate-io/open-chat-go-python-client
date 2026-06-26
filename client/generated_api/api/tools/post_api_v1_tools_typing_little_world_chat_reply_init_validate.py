from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.little_world_chat_reply_init import LittleWorldChatReplyInit
from ...models.tools_tool_validate_payload_response import ToolsToolValidatePayloadResponse
from typing import cast



def _get_kwargs(
    *,
    body: LittleWorldChatReplyInit,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tools/typing/little_world__chat_reply/init/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ToolsToolValidatePayloadResponse | None:
    if response.status_code == 200:
        response_200 = ToolsToolValidatePayloadResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ToolsToolValidatePayloadResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LittleWorldChatReplyInit,

) -> Response[Any | ToolsToolValidatePayloadResponse]:
    """ Validate little_world__chat_reply init payload

     Validate payload for tool `little_world__chat_reply` init configuration.

    Args:
        body (LittleWorldChatReplyInit): Initialization data required to authenticate and target
            the Little World chat API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ToolsToolValidatePayloadResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: LittleWorldChatReplyInit,

) -> Any | ToolsToolValidatePayloadResponse | None:
    """ Validate little_world__chat_reply init payload

     Validate payload for tool `little_world__chat_reply` init configuration.

    Args:
        body (LittleWorldChatReplyInit): Initialization data required to authenticate and target
            the Little World chat API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ToolsToolValidatePayloadResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: LittleWorldChatReplyInit,

) -> Response[Any | ToolsToolValidatePayloadResponse]:
    """ Validate little_world__chat_reply init payload

     Validate payload for tool `little_world__chat_reply` init configuration.

    Args:
        body (LittleWorldChatReplyInit): Initialization data required to authenticate and target
            the Little World chat API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ToolsToolValidatePayloadResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: LittleWorldChatReplyInit,

) -> Any | ToolsToolValidatePayloadResponse | None:
    """ Validate little_world__chat_reply init payload

     Validate payload for tool `little_world__chat_reply` init configuration.

    Args:
        body (LittleWorldChatReplyInit): Initialization data required to authenticate and target
            the Little World chat API.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ToolsToolValidatePayloadResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
