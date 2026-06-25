from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user_user_login import UserUserLogin
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: UserUserLogin,
    cookie_origin: str | Unset = UNSET,
    cookie_domain: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["cookie_origin"] = cookie_origin

    params["cookie_domain"] = cookie_domain


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/user/login",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> str | None:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if response.status_code == 500:
        response_500 = cast(str, response.json())
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserUserLogin,
    cookie_origin: str | Unset = UNSET,
    cookie_domain: str | Unset = UNSET,

) -> Response[str]:
    """ Login a user

     Authenticate and login a user with email and password

    Args:
        cookie_origin (str | Unset):
        cookie_domain (str | Unset):
        body (UserUserLogin):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
     """


    kwargs = _get_kwargs(
        body=body,
cookie_origin=cookie_origin,
cookie_domain=cookie_domain,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: UserUserLogin,
    cookie_origin: str | Unset = UNSET,
    cookie_domain: str | Unset = UNSET,

) -> str | None:
    """ Login a user

     Authenticate and login a user with email and password

    Args:
        cookie_origin (str | Unset):
        cookie_domain (str | Unset):
        body (UserUserLogin):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
     """


    return sync_detailed(
        client=client,
body=body,
cookie_origin=cookie_origin,
cookie_domain=cookie_domain,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserUserLogin,
    cookie_origin: str | Unset = UNSET,
    cookie_domain: str | Unset = UNSET,

) -> Response[str]:
    """ Login a user

     Authenticate and login a user with email and password

    Args:
        cookie_origin (str | Unset):
        cookie_domain (str | Unset):
        body (UserUserLogin):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
     """


    kwargs = _get_kwargs(
        body=body,
cookie_origin=cookie_origin,
cookie_domain=cookie_domain,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserUserLogin,
    cookie_origin: str | Unset = UNSET,
    cookie_domain: str | Unset = UNSET,

) -> str | None:
    """ Login a user

     Authenticate and login a user with email and password

    Args:
        cookie_origin (str | Unset):
        cookie_domain (str | Unset):
        body (UserUserLogin):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
     """


    return (await asyncio_detailed(
        client=client,
body=body,
cookie_origin=cookie_origin,
cookie_domain=cookie_domain,

    )).parsed
