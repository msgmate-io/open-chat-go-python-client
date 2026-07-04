from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.integrations_integration_overview_response import IntegrationsIntegrationOverviewResponse
from typing import cast



def _get_kwargs(
    integration_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/integrations/{integration_name}/overview".format(integration_name=quote(str(integration_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IntegrationsIntegrationOverviewResponse | str | None:
    if response.status_code == 200:
        response_200 = IntegrationsIntegrationOverviewResponse.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IntegrationsIntegrationOverviewResponse | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[IntegrationsIntegrationOverviewResponse | str]:
    """ Get integration overview

     Returns API routes, registered model types and function names for a compiled integration.

    Args:
        integration_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsIntegrationOverviewResponse | str]
     """


    kwargs = _get_kwargs(
        integration_name=integration_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    integration_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> IntegrationsIntegrationOverviewResponse | str | None:
    """ Get integration overview

     Returns API routes, registered model types and function names for a compiled integration.

    Args:
        integration_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsIntegrationOverviewResponse | str
     """


    return sync_detailed(
        integration_name=integration_name,
client=client,

    ).parsed

async def asyncio_detailed(
    integration_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[IntegrationsIntegrationOverviewResponse | str]:
    """ Get integration overview

     Returns API routes, registered model types and function names for a compiled integration.

    Args:
        integration_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntegrationsIntegrationOverviewResponse | str]
     """


    kwargs = _get_kwargs(
        integration_name=integration_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    integration_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> IntegrationsIntegrationOverviewResponse | str | None:
    """ Get integration overview

     Returns API routes, registered model types and function names for a compiled integration.

    Args:
        integration_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IntegrationsIntegrationOverviewResponse | str
     """


    return (await asyncio_detailed(
        integration_name=integration_name,
client=client,

    )).parsed
