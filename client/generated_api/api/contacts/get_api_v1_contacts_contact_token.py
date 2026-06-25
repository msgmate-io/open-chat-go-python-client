from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.contacts_listed_contact import ContactsListedContact
from typing import cast



def _get_kwargs(
    contact_token: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/contacts/{contact_token}".format(contact_token=quote(str(contact_token), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ContactsListedContact | str | None:
    if response.status_code == 200:
        response_200 = ContactsListedContact.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ContactsListedContact | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_token: str,
    *,
    client: AuthenticatedClient,

) -> Response[ContactsListedContact | str]:
    """ Get contact by token

     Retrieve a single contact by their contact token

    Args:
        contact_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsListedContact | str]
     """


    kwargs = _get_kwargs(
        contact_token=contact_token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    contact_token: str,
    *,
    client: AuthenticatedClient,

) -> ContactsListedContact | str | None:
    """ Get contact by token

     Retrieve a single contact by their contact token

    Args:
        contact_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsListedContact | str
     """


    return sync_detailed(
        contact_token=contact_token,
client=client,

    ).parsed

async def asyncio_detailed(
    contact_token: str,
    *,
    client: AuthenticatedClient,

) -> Response[ContactsListedContact | str]:
    """ Get contact by token

     Retrieve a single contact by their contact token

    Args:
        contact_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContactsListedContact | str]
     """


    kwargs = _get_kwargs(
        contact_token=contact_token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    contact_token: str,
    *,
    client: AuthenticatedClient,

) -> ContactsListedContact | str | None:
    """ Get contact by token

     Retrieve a single contact by their contact token

    Args:
        contact_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContactsListedContact | str
     """


    return (await asyncio_detailed(
        contact_token=contact_token,
client=client,

    )).parsed
