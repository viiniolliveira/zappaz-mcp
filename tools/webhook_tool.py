from fastmcp import FastMCP, Context
from zappaz.webhook import *
from schemas.webhook_chema import *

mcp = FastMCP()

@mcp.tool(
    name="get_webhooks", 
    description="Obtém a lista de webhooks configurados para uma sessão na Zappaz API",
)
async def get_webhooks_tool(ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await get_webhooks(
        token=session_token,
        sessionId=session_id,
    )

    return res


@mcp.tool(
    name="create_webhook", 
    description="Cria um novo webhook para uma sessão na Zappaz API",
)
async def create_webhook_tool(data: Webhook, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await create_webhook(
        token=session_token,
        sessionId=session_id,
        data=data,
    )

    return res


@mcp.tool(
    name="update_webhook", 
    description="Atualiza um webhook existente para uma sessão na Zappaz API",
)
async def update_webhook_tool(webhookId: str, data: Webhook, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await update_webhook(
        token=session_token,
        sessionId=session_id,
        webhookId=webhookId,
        data=data,
    )

    return res

@mcp.tool(
    name="delete_webhook", 
    description="Deleta um webhook existente para uma sessão na Zappaz API",
)
async def delete_webhook_tool(webhookId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")

    res = await delete_webhook(
        token=session_token,
        sessionId=session_id,
        webhookId=webhookId,
    )

    return res