from fastmcp import FastMCP, Context
from zappaz.message import (
    send_document_message,
    send_text_message, 
    send_image_message,
    send_video_message,
    send_audio_message,
    send_contact_message,
    send_location_message,
    delete_message
)
from schemas.message_schema import *

mcp = FastMCP()

@mcp.tool(
    name="send_text_message", 
    description="Envia uma mensagem de texto atraves da Zappaz API",
)
async def send_text_message_tool(data: TextMessage, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")
    res = await send_text_message(
        token=session_token,
        sessionId=session_id,
        data=data,
    )
    return res


@mcp.tool(
    name="send_image_message", 
    description="Envia uma mensagem de imagem atraves da Zappaz API",
)
async def send_image_message_tool(data: ImageMessage, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")
    res = await send_image_message(
        token=session_token,
        sessionId=session_id,
        data=data,
    )
    return res


@mcp.tool(
    name="send_video_message", 
    description="Envia uma mensagem de vídeo atraves da Zappaz API",
)
async def send_video_message_tool(data: VideoMessage, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")
    res = await send_video_message(
        token=session_token,
        sessionId=session_id,
        data=data,
    )
    return res  



@mcp.tool(
    name="send_audio_message", 
    description="Envia uma mensagem de áudio atraves da Zappaz API",
)
async def send_audio_message_tool(data: AudioMessage, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")
    res = await send_audio_message(
        token=session_token,
        sessionId=session_id,
        data=data,
    )
    return res


@mcp.tool(
    name="send_document_message", 
    description="Envia uma mensagem de documento atraves da Zappaz API",
)
async def send_document_message_tool(data: DocumentMessage, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")
    res = await send_document_message(
        token=session_token,
        sessionId=session_id,
        data=data,
    )
    return res



@mcp.tool(
    name="send_contact_message", 
    description="Envia uma mensagem com um contato atraves da Zappaz API",
)
async def send_contact_message_tool(data: ContactMessage, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")
    res = await send_contact_message(
        token=session_token,
        sessionId=session_id,
        data=data,
    )
    return res


@mcp.tool(
    name="send_location_message", 
    description="Envia uma mensagem com uma localização por endereço ou coordenadas atraves da Zappaz API",
)
async def send_location_message_tool(data: LocationMessage, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")
    res = await send_location_message(
        token=session_token,
        sessionId=session_id,
        data=data,
    )
    return res


@mcp.tool(
    name="delete_message", 
    description="Deleta uma mensagem atraves da Zappaz API",
)
async def delete_message_tool(messageId: str, ctx: Context):
    session_id = await ctx.get_state("session_id")
    session_token = await ctx.get_state("session_token")
    res = await delete_message(
        token=session_token,
        sessionId=session_id,
        messageId=messageId,
    )
    return res