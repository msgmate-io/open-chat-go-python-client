from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bots_bot_interaction_response import BotsBotInteractionResponse
from ...models.bots_create_bot_interaction_request import BotsCreateBotInteractionRequest
from typing import cast



def _get_kwargs(
    identifier: str,
    *,
    body: BotsCreateBotInteractionRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/bots/{identifier}/interactions".format(identifier=quote(str(identifier), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BotsBotInteractionResponse | str | None:
    if response.status_code == 200:
        response_200 = BotsBotInteractionResponse.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BotsBotInteractionResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient,
    body: BotsCreateBotInteractionRequest,

) -> Response[BotsBotInteractionResponse | str]:
    """ Create bot interaction

     Create an interaction chat for the specified bot using default config + overrides

    Args:
        identifier (str):
        body (BotsCreateBotInteractionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotsBotInteractionResponse | str]
     """


    kwargs = _get_kwargs(
        identifier=identifier,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    identifier: str,
    *,
    client: AuthenticatedClient,
    body: BotsCreateBotInteractionRequest,

) -> BotsBotInteractionResponse | str | None:
    """ Create bot interaction

     Create an interaction chat for the specified bot using default config + overrides

    Args:
        identifier (str):
        body (BotsCreateBotInteractionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotsBotInteractionResponse | str
     """


    return sync_detailed(
        identifier=identifier,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    identifier: str,
    *,
    client: AuthenticatedClient,
    body: BotsCreateBotInteractionRequest,

) -> Response[BotsBotInteractionResponse | str]:
    """ Create bot interaction

     Create an interaction chat for the specified bot using default config + overrides

    Args:
        identifier (str):
        body (BotsCreateBotInteractionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotsBotInteractionResponse | str]
     """


    kwargs = _get_kwargs(
        identifier=identifier,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    identifier: str,
    *,
    client: AuthenticatedClient,
    body: BotsCreateBotInteractionRequest,

) -> BotsBotInteractionResponse | str | None:
    """ Create bot interaction

     Create an interaction chat for the specified bot using default config + overrides

    Args:
        identifier (str):
        body (BotsCreateBotInteractionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotsBotInteractionResponse | str
     """


    return (await asyncio_detailed(
        identifier=identifier,
client=client,
body=body,

    )).parsed
