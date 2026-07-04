from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_api_v1_integrations_rest_api_tool_tools_tool_name_response_200 import DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200
from typing import cast



def _get_kwargs(
    tool_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/integrations/rest_api_tool/tools/{tool_name}".format(tool_name=quote(str(tool_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200 | None:
    if response.status_code == 200:
        response_200 = DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tool_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200]:
    """ Delete REST API tool

     Delete an owner-scoped runtime REST API tool definition.

    Args:
        tool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tool_name: str,
    *,
    client: AuthenticatedClient,

) -> DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200 | None:
    """ Delete REST API tool

     Delete an owner-scoped runtime REST API tool definition.

    Args:
        tool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200
     """


    return sync_detailed(
        tool_name=tool_name,
client=client,

    ).parsed

async def asyncio_detailed(
    tool_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200]:
    """ Delete REST API tool

     Delete an owner-scoped runtime REST API tool definition.

    Args:
        tool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200]
     """


    kwargs = _get_kwargs(
        tool_name=tool_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tool_name: str,
    *,
    client: AuthenticatedClient,

) -> DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200 | None:
    """ Delete REST API tool

     Delete an owner-scoped runtime REST API tool definition.

    Args:
        tool_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteApiV1IntegrationsRestApiToolToolsToolNameResponse200
     """


    return (await asyncio_detailed(
        tool_name=tool_name,
client=client,

    )).parsed
