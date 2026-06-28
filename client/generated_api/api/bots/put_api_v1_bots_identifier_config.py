from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bots_bot_dto import BotsBotDTO
from ...models.put_api_v1_bots_identifier_config_body import PutApiV1BotsIdentifierConfigBody
from typing import cast



def _get_kwargs(
    identifier: str,
    *,
    body: PutApiV1BotsIdentifierConfigBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/bots/{identifier}/config".format(identifier=quote(str(identifier), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BotsBotDTO | str | None:
    if response.status_code == 200:
        response_200 = BotsBotDTO.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BotsBotDTO | str]:
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
    body: PutApiV1BotsIdentifierConfigBody,

) -> Response[BotsBotDTO | str]:
    """ Save bot config

     Replace bot default_shared_config after strict structure validation

    Args:
        identifier (str):
        body (PutApiV1BotsIdentifierConfigBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotsBotDTO | str]
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
    body: PutApiV1BotsIdentifierConfigBody,

) -> BotsBotDTO | str | None:
    """ Save bot config

     Replace bot default_shared_config after strict structure validation

    Args:
        identifier (str):
        body (PutApiV1BotsIdentifierConfigBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotsBotDTO | str
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
    body: PutApiV1BotsIdentifierConfigBody,

) -> Response[BotsBotDTO | str]:
    """ Save bot config

     Replace bot default_shared_config after strict structure validation

    Args:
        identifier (str):
        body (PutApiV1BotsIdentifierConfigBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BotsBotDTO | str]
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
    body: PutApiV1BotsIdentifierConfigBody,

) -> BotsBotDTO | str | None:
    """ Save bot config

     Replace bot default_shared_config after strict structure validation

    Args:
        identifier (str):
        body (PutApiV1BotsIdentifierConfigBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BotsBotDTO | str
     """


    return (await asyncio_detailed(
        identifier=identifier,
client=client,
body=body,

    )).parsed
