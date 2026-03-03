from schemas.group_schema import *
from zappaz.zappaz_client import client, get_headers
from zappaz.utils import get_participants
from fastmcp.exceptions import ToolError
from mcp.types import ErrorData


async def list_groups(sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.get(url=f"/session/{sessionId}/group", headers=headers)

    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))

    content = response.json()

    res = {
        "totalGroups": len(content),
        "groups": [
            {
                **{key: value for key, value in group.items() if key != "participants"},
                "totalParticipants": len(group.get("participants", [])),
            }
            for group in content
        ],
    }

    return res


async def get_group_participants(groupId: str, sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.get(url=f"/session/{sessionId}/group", headers=headers)

    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))

    content = response.json()

    participants = get_participants(content, groupId)

    return {
        "groupId": groupId,
        "totalParticipants": len(participants),
        "participants": participants,
    }


async def create_group(data: CreateGroup, sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.post(
        url=f"/session/{sessionId}/group", json=data.model_dump(), headers=headers
    )

    if response.status_code != 201:
        return ToolError(ErrorData(message=response.text, code=response.status_code))

    return response.json()


async def remove_participants(
    data: PhoneList, groupId: str, sessionId: str, token: str
):
    headers = get_headers(token)
    response = await client.post(
        url=f"/session/{sessionId}/group/{groupId}/remove",
        json=data.model_dump(),
        headers=headers,
    )
    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))
    return response.json()


async def add_participants(data: PhoneList, groupId: str, sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.post(
        url=f"/session/{sessionId}/group/{groupId}/add",
        json=data.model_dump(),
        headers=headers,
    )
    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))
    return response.json()


async def promote_participants(
    data: PhoneList, groupId: str, sessionId: str, token: str
):
    headers = get_headers(token)
    response = await client.post(
        url=f"/session/{sessionId}/group/{groupId}/promote",
        json=data.model_dump(),
        headers=headers,
    )
    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))
    return response.json()


async def demote_participants(
    data: PhoneList, groupId: str, sessionId: str, token: str
):
    headers = get_headers(token)
    response = await client.post(
        url=f"/session/{sessionId}/group/{groupId}/demote",
        json=data.model_dump(),
        headers=headers,
    )
    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))
    return response.json()


async def send_group_invite_link(
    data: InviteLink, groupId: str, sessionId: str, token: str
):
    headers = get_headers(token)
    response = await client.post(
        url=f"/session/{sessionId}/group/{groupId}/send-invite",
        json=data.model_dump(),
        headers=headers,
    )
    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))
    return response.json()


async def update_group(data: UpdateGroup, groupId: str, sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.put(
        url=f"/session/{sessionId}/group/{groupId}",
        json=data.model_dump(),
        headers=headers,
    )
    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))
    return response.json()


async def update_group_picture(data: UpdateGroupPicture, sessionId: str, token: str):
    headers = get_headers(token)
    response = await client.put(
        url=f"/session/{sessionId}/display-picture",
        json=data.model_dump(),
        headers=headers,
    )
    if response.status_code != 200:
        return ToolError(ErrorData(message=response.text, code=response.status_code))
    return response.json()
