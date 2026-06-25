from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_api_v1_interactions_chat_uuid_tools_init_response_200 import PostApiV1InteractionsChatUuidToolsInitResponse200
from ...models.post_api_v1_interactions_chat_uuid_tools_init_response_400 import PostApiV1InteractionsChatUuidToolsInitResponse400
from ...models.post_api_v1_interactions_chat_uuid_tools_init_response_403 import PostApiV1InteractionsChatUuidToolsInitResponse403
from ...models.post_api_v1_interactions_chat_uuid_tools_init_response_404 import PostApiV1InteractionsChatUuidToolsInitResponse404
from ...models.tools_store_tool_init_data_request import ToolsStoreToolInitDataRequest
from typing import cast



def _get_kwargs(
    chat_uuid: str,
    *,
    body: ToolsStoreToolInitDataRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/interactions/{chat_uuid}/tools/init".format(chat_uuid=quote(str(chat_uuid), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404 | None:
    if response.status_code == 200:
        response_200 = PostApiV1InteractionsChatUuidToolsInitResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostApiV1InteractionsChatUuidToolsInitResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = PostApiV1InteractionsChatUuidToolsInitResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostApiV1InteractionsChatUuidToolsInitResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404]:
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
    body: ToolsStoreToolInitDataRequest,

) -> Response[PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404]:
    """ Store tool initialization data

     Store tool initialization data for a specific chat and tool (bot users only)

    Args:
        chat_uuid (str):
        body (ToolsStoreToolInitDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404]
     """


    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolsStoreToolInitDataRequest,

) -> PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404 | None:
    """ Store tool initialization data

     Store tool initialization data for a specific chat and tool (bot users only)

    Args:
        chat_uuid (str):
        body (ToolsStoreToolInitDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404
     """


    return sync_detailed(
        chat_uuid=chat_uuid,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolsStoreToolInitDataRequest,

) -> Response[PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404]:
    """ Store tool initialization data

     Store tool initialization data for a specific chat and tool (bot users only)

    Args:
        chat_uuid (str):
        body (ToolsStoreToolInitDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404]
     """


    kwargs = _get_kwargs(
        chat_uuid=chat_uuid,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    chat_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    body: ToolsStoreToolInitDataRequest,

) -> PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404 | None:
    """ Store tool initialization data

     Store tool initialization data for a specific chat and tool (bot users only)

    Args:
        chat_uuid (str):
        body (ToolsStoreToolInitDataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostApiV1InteractionsChatUuidToolsInitResponse200 | PostApiV1InteractionsChatUuidToolsInitResponse400 | PostApiV1InteractionsChatUuidToolsInitResponse403 | PostApiV1InteractionsChatUuidToolsInitResponse404
     """


    return (await asyncio_detailed(
        chat_uuid=chat_uuid,
client=client,
body=body,

    )).parsed
