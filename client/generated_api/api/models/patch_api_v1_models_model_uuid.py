from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.models_model_list_item import ModelsModelListItem
from ...models.models_model_patch_request import ModelsModelPatchRequest
from typing import cast



def _get_kwargs(
    model_uuid: str,
    *,
    body: ModelsModelPatchRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/models/{model_uuid}".format(model_uuid=quote(str(model_uuid), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ModelsModelListItem | str | None:
    if response.status_code == 200:
        response_200 = ModelsModelListItem.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(str, response.json())
        return response_400

    if response.status_code == 403:
        response_403 = cast(str, response.json())
        return response_403

    if response.status_code == 404:
        response_404 = cast(str, response.json())
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ModelsModelListItem | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    model_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModelsModelPatchRequest,

) -> Response[ModelsModelListItem | str]:
    """ Patch model

     Update a model row by UUID. Owner or admin only.

    Args:
        model_uuid (str):
        body (ModelsModelPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsModelListItem | str]
     """


    kwargs = _get_kwargs(
        model_uuid=model_uuid,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    model_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModelsModelPatchRequest,

) -> ModelsModelListItem | str | None:
    """ Patch model

     Update a model row by UUID. Owner or admin only.

    Args:
        model_uuid (str):
        body (ModelsModelPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsModelListItem | str
     """


    return sync_detailed(
        model_uuid=model_uuid,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    model_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModelsModelPatchRequest,

) -> Response[ModelsModelListItem | str]:
    """ Patch model

     Update a model row by UUID. Owner or admin only.

    Args:
        model_uuid (str):
        body (ModelsModelPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ModelsModelListItem | str]
     """


    kwargs = _get_kwargs(
        model_uuid=model_uuid,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    model_uuid: str,
    *,
    client: AuthenticatedClient | Client,
    body: ModelsModelPatchRequest,

) -> ModelsModelListItem | str | None:
    """ Patch model

     Update a model row by UUID. Owner or admin only.

    Args:
        model_uuid (str):
        body (ModelsModelPatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ModelsModelListItem | str
     """


    return (await asyncio_detailed(
        model_uuid=model_uuid,
client=client,
body=body,

    )).parsed
