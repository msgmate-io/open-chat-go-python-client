from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.models_models_list_response import ModelsModelsListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    hoster: str | Unset = UNSET,
    source: str | Unset = UNSET,
    q: str | Unset = UNSET,
    bot: str | Unset = UNSET,
    bot_uuid: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["page_size"] = page_size

    params["hoster"] = hoster

    params["source"] = source

    params["q"] = q

    params["bot"] = bot

    params["bot_uuid"] = bot_uuid


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/models/list",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ModelsModelsListResponse | None:
    if response.status_code == 200:
        response_200 = ModelsModelsListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ModelsModelsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    hoster: str | Unset = UNSET,
    source: str | Unset = UNSET,
    q: str | Unset = UNSET,
    bot: str | Unset = UNSET,
    bot_uuid: str | Unset = UNSET,

) -> Response[ModelsModelsListResponse]:
    """ List models

     List model configurations with pagination and filters. Guests receive restricted fields, admins
    receive extended metadata.

    Args:
        page (int | Unset):
        page_size (int | Unset):
        hoster (str | Unset):
        source (str | Unset):
        q (str | Unset):
        bot (str | Unset):
        bot_uuid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsModelsListResponse]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
hoster=hoster,
source=source,
q=q,
bot=bot,
bot_uuid=bot_uuid,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    hoster: str | Unset = UNSET,
    source: str | Unset = UNSET,
    q: str | Unset = UNSET,
    bot: str | Unset = UNSET,
    bot_uuid: str | Unset = UNSET,

) -> ModelsModelsListResponse | None:
    """ List models

     List model configurations with pagination and filters. Guests receive restricted fields, admins
    receive extended metadata.

    Args:
        page (int | Unset):
        page_size (int | Unset):
        hoster (str | Unset):
        source (str | Unset):
        q (str | Unset):
        bot (str | Unset):
        bot_uuid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsModelsListResponse
     """


    return sync_detailed(
        client=client,
page=page,
page_size=page_size,
hoster=hoster,
source=source,
q=q,
bot=bot,
bot_uuid=bot_uuid,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    hoster: str | Unset = UNSET,
    source: str | Unset = UNSET,
    q: str | Unset = UNSET,
    bot: str | Unset = UNSET,
    bot_uuid: str | Unset = UNSET,

) -> Response[ModelsModelsListResponse]:
    """ List models

     List model configurations with pagination and filters. Guests receive restricted fields, admins
    receive extended metadata.

    Args:
        page (int | Unset):
        page_size (int | Unset):
        hoster (str | Unset):
        source (str | Unset):
        q (str | Unset):
        bot (str | Unset):
        bot_uuid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsModelsListResponse]
     """


    kwargs = _get_kwargs(
        page=page,
page_size=page_size,
hoster=hoster,
source=source,
q=q,
bot=bot,
bot_uuid=bot_uuid,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    page_size: int | Unset = UNSET,
    hoster: str | Unset = UNSET,
    source: str | Unset = UNSET,
    q: str | Unset = UNSET,
    bot: str | Unset = UNSET,
    bot_uuid: str | Unset = UNSET,

) -> ModelsModelsListResponse | None:
    """ List models

     List model configurations with pagination and filters. Guests receive restricted fields, admins
    receive extended metadata.

    Args:
        page (int | Unset):
        page_size (int | Unset):
        hoster (str | Unset):
        source (str | Unset):
        q (str | Unset):
        bot (str | Unset):
        bot_uuid (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsModelsListResponse
     """


    return (await asyncio_detailed(
        client=client,
page=page,
page_size=page_size,
hoster=hoster,
source=source,
q=q,
bot=bot,
bot_uuid=bot_uuid,

    )).parsed
