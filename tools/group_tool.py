from fastmcp import FastMCP, Context
from zappaz.group import *

mcp = FastMCP()

@mcp.tool(
    name="list_groups", 
    description="Lista todos os grupos de uma sessão na Zappaz API",
)
async def list_groups_tool(ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await list_groups(
        token=session_token,
        sessionId=session_id,
    )

    return res


@mcp.tool(
    name="get_group_participants", 
    description="Obtém a lista de participantes de um grupo específico na Zappaz API",
)
async def get_group_participants_tool(groupId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await get_group_participants(
        token=session_token,
        sessionId=session_id,
        groupId=groupId,
    )

    return res



@mcp.tool(
    name="create_group", 
    description="Cria um novo grupo na Zappaz API",
)
async def create_group_tool(data: CreateGroup, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await create_group(
        token=session_token,
        sessionId=session_id,
        data=data,
    )

    return res


@mcp.tool(
    name="remove_participants", 
    description="Remove participantes de um grupo na Zappaz API",
)
async def remove_participants_tool(data: PhoneList, groupId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await remove_participants(
        token=session_token,
        sessionId=session_id,
        groupId=groupId,
        data=data,
    )

    return res


@mcp.tool(
    name="add_participants", 
    description="Adiciona participantes a um grupo na Zappaz API",
)
async def add_participants_tool(data: PhoneList, groupId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await add_participants(
        token=session_token,
        sessionId=session_id,
        groupId=groupId,
        data=data,
    )

    return res


@mcp.tool(
    name="promote_participants", 
    description="Promove participantes a administradores de um grupo na Zappaz API",
)
async def promote_participants_tool(data: PhoneList, groupId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await promote_participants(
        token=session_token,
        sessionId=session_id,
        groupId=groupId,
        data=data,
    )

    return res


@mcp.tool(
    name="demote_participants", 
    description="Rebaixa participantes de administradores a membros de um grupo na Zappaz API",
)
async def demote_participants_tool(data: PhoneList, groupId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await demote_participants(
        token=session_token,
        sessionId=session_id,
        groupId=groupId,
        data=data,
    )

    return res


@mcp.tool(
    name="send_group_invite_link", 
    description="Envia o link de convite de um grupo específico na Zappaz API",
)
async def send_group_invite_link_tool(data: InviteLink, groupId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await send_group_invite_link(
        token=session_token,
        sessionId=session_id,
        groupId=groupId,
        data=data,
    )

    return res


@mcp.tool(
    name="update_group", 
    description="Atualiza as informações de um grupo específico na Zappaz API",
)
async def update_group_tool(data: UpdateGroup, groupId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await update_group(
        token=session_token,
        sessionId=session_id,
        groupId=groupId,
        data=data,
    )

    return res


@mcp.tool(
    name="update_group_picture", 
    description="Atualiza a foto de um grupo específico na Zappaz API",
)
async def update_group_picture_tool(data: UpdateGroupPicture, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await update_group_picture(
        token=session_token,
        sessionId=session_id,
        data=data,
    )

    return res
