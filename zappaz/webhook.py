from schemas.group_schema import *
from zappaz.zappaz_client import client, get_headers
from schemas.webhook_chema import *
from fastmcp.exceptions import ToolError
from mcp.types import ErrorData


async def get_webhooks(sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.get(url=f"/session/{sessionId}/webhook", headers=headers)

    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))

    return response.json()


async def create_webhook(data: Webhook, sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.post(
        url=f"/session/{sessionId}/webhook",
        json=data.model_dump(by_alias=True, exclude_none=True),
        headers=headers,
    )

    if response.status_code != 201:
        return ToolError(ErrorData(message=response.text, code=response.status_code))

    return response.json()


async def update_webhook(webhookId: str, data: Webhook, sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.put(
        url=f"/session/{sessionId}/webhook/{webhookId}",
        json=data.model_dump(by_alias=True, exclude_none=True),
        headers=headers,
    )

    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))

    return response.json()


async def delete_webhook(webhookId: str, sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.delete(
        url=f"/session/{sessionId}/webhook/{webhookId}",
        headers=headers,
    )

    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))

    return {"message": "Webhook deleted successfully"}