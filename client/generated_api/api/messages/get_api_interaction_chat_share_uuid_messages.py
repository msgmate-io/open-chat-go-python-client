from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.database_pagination import DatabasePagination
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    chat_share_uuid: str,
    *,
    page: int | Unset = 1,
    limit: int | Unset = 40,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/interaction/{chat_share_uuid}/messages".format(chat_share_uuid=quote(str(chat_share_uuid), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DatabasePagination | str | None:
    if response.status_code == 200:
        response_200 = DatabasePagination.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DatabasePagination | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_share_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 40,

) -> Response[DatabasePagination | str]:
    """ List shared interaction messages

     Retrieve paginated messages for a shared interaction chat

    Args:
        chat_share_uuid (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabasePagination | str]
     """


    kwargs = _get_kwargs(
        chat_share_uuid=chat_share_uuid,
page=page,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    chat_share_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 40,

) -> DatabasePagination | str | None:
    """ List shared interaction messages

     Retrieve paginated messages for a shared interaction chat

    Args:
        chat_share_uuid (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabasePagination | str
     """


    return sync_detailed(
        chat_share_uuid=chat_share_uuid,
client=client,
page=page,
limit=limit,

    ).parsed

async def asyncio_detailed(
    chat_share_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 40,

) -> Response[DatabasePagination | str]:
    """ List shared interaction messages

     Retrieve paginated messages for a shared interaction chat

    Args:
        chat_share_uuid (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DatabasePagination | str]
     """


    kwargs = _get_kwargs(
        chat_share_uuid=chat_share_uuid,
page=page,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    chat_share_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 40,

) -> DatabasePagination | str | None:
    """ List shared interaction messages

     Retrieve paginated messages for a shared interaction chat

    Args:
        chat_share_uuid (str):
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 40.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DatabasePagination | str
     """


    return (await asyncio_detailed(
        chat_share_uuid=chat_share_uuid,
client=client,
page=page,
limit=limit,

    )).parsed
