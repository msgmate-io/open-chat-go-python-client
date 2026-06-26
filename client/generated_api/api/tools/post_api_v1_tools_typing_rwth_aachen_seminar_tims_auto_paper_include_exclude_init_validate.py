from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_api_v1_tools_typing_rwth_aachen_seminar_tims_auto_paper_include_exclude_init_validate_response_200 import PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200
from ...models.rwth_aachen_seminar_tims_auto_paper_include_exclude_init import RwthAachenSeminarTimsAutoPaperIncludeExcludeInit
from typing import cast



def _get_kwargs(
    *,
    body: RwthAachenSeminarTimsAutoPaperIncludeExcludeInit,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/tools/typing/rwth_aachen_seminar_tims_auto_paper_include_exclude/init/validate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RwthAachenSeminarTimsAutoPaperIncludeExcludeInit,

) -> Response[Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200]:
    """ Validate rwth_aachen_seminar_tims_auto_paper_include_exclude init payload

     Validate payload for tool `rwth_aachen_seminar_tims_auto_paper_include_exclude` init configuration.

    Args:
        body (RwthAachenSeminarTimsAutoPaperIncludeExcludeInit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RwthAachenSeminarTimsAutoPaperIncludeExcludeInit,

) -> Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200 | None:
    """ Validate rwth_aachen_seminar_tims_auto_paper_include_exclude init payload

     Validate payload for tool `rwth_aachen_seminar_tims_auto_paper_include_exclude` init configuration.

    Args:
        body (RwthAachenSeminarTimsAutoPaperIncludeExcludeInit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RwthAachenSeminarTimsAutoPaperIncludeExcludeInit,

) -> Response[Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200]:
    """ Validate rwth_aachen_seminar_tims_auto_paper_include_exclude init payload

     Validate payload for tool `rwth_aachen_seminar_tims_auto_paper_include_exclude` init configuration.

    Args:
        body (RwthAachenSeminarTimsAutoPaperIncludeExcludeInit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RwthAachenSeminarTimsAutoPaperIncludeExcludeInit,

) -> Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200 | None:
    """ Validate rwth_aachen_seminar_tims_auto_paper_include_exclude init payload

     Validate payload for tool `rwth_aachen_seminar_tims_auto_paper_include_exclude` init configuration.

    Args:
        body (RwthAachenSeminarTimsAutoPaperIncludeExcludeInit):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostApiV1ToolsTypingRwthAachenSeminarTimsAutoPaperIncludeExcludeInitValidateResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
