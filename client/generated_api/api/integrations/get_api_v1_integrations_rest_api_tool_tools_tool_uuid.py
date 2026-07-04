from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.restapitoolintegration_dynamic_rest_tool_detail_response import RestapitoolintegrationDynamicRESTToolDetailResponse
from typing import cast



def _get_kwargs(
    tool_uuid: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/integrations/rest_api_tool/tools/{tool_uuid}".format(tool_uuid=quote(str(tool_uuid), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RestapitoolintegrationDynamicRESTToolDetailResponse | None:
    if response.status_code == 200:
        response_200 = RestapitoolintegrationDynamicRESTToolDetailResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RestapitoolintegrationDynamicRESTToolDetailResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tool_uuid: str,
    *,
    client: AuthenticatedClient,

) -> Response[RestapitoolintegrationDynamicRESTToolDetailResponse]:
    """ Get REST API tool

     Get one owner-scoped runtime REST API tool by UUID.

    Args:
        tool_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestapitoolintegrationDynamicRESTToolDetailResponse]
     """


    kwargs = _get_kwargs(
        tool_uuid=tool_uuid,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    tool_uuid: str,
    *,
    client: AuthenticatedClient,

) -> RestapitoolintegrationDynamicRESTToolDetailResponse | None:
    """ Get REST API tool

     Get one owner-scoped runtime REST API tool by UUID.

    Args:
        tool_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestapitoolintegrationDynamicRESTToolDetailResponse
     """


    return sync_detailed(
        tool_uuid=tool_uuid,
client=client,

    ).parsed

async def asyncio_detailed(
    tool_uuid: str,
    *,
    client: AuthenticatedClient,

) -> Response[RestapitoolintegrationDynamicRESTToolDetailResponse]:
    """ Get REST API tool

     Get one owner-scoped runtime REST API tool by UUID.

    Args:
        tool_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RestapitoolintegrationDynamicRESTToolDetailResponse]
     """


    kwargs = _get_kwargs(
        tool_uuid=tool_uuid,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    tool_uuid: str,
    *,
    client: AuthenticatedClient,

) -> RestapitoolintegrationDynamicRESTToolDetailResponse | None:
    """ Get REST API tool

     Get one owner-scoped runtime REST API tool by UUID.

    Args:
        tool_uuid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RestapitoolintegrationDynamicRESTToolDetailResponse
     """


    return (await asyncio_detailed(
        tool_uuid=tool_uuid,
client=client,

    )).parsed
