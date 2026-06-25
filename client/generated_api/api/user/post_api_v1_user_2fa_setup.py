from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.user_two_factor_setup_response import UserTwoFactorSetupResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/user/2fa/setup",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UserTwoFactorSetupResponse | str | None:
    if response.status_code == 200:
        response_200 = UserTwoFactorSetupResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UserTwoFactorSetupResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[UserTwoFactorSetupResponse | str]:
    """ Setup Two-Factor Authentication

     Generate a new 2FA secret and QR code URL for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserTwoFactorSetupResponse | str]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> UserTwoFactorSetupResponse | str | None:
    """ Setup Two-Factor Authentication

     Generate a new 2FA secret and QR code URL for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserTwoFactorSetupResponse | str
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[UserTwoFactorSetupResponse | str]:
    """ Setup Two-Factor Authentication

     Generate a new 2FA secret and QR code URL for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserTwoFactorSetupResponse | str]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> UserTwoFactorSetupResponse | str | None:
    """ Setup Two-Factor Authentication

     Generate a new 2FA secret and QR code URL for the user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserTwoFactorSetupResponse | str
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
