import asyncio
from fastmcp import FastMCP
from middlewares.auth_middleware import AuthSessionMiddleware
from middlewares.ratelimit_middleware import RateLimitMiddleware
from tools.message_tool import (
    send_text_message_tool, 
    send_image_message_tool,
    send_video_message_tool,
    send_audio_message_tool,
    send_document_message_tool,
    send_contact_message_tool,
    send_location_message_tool,
    delete_message_tool
)

mcp = FastMCP(
    name="Zappaz MCP",
    instructions="Este é um mcp server da zappaz api uma api de WhatsApp, que da acesso a todas as funcionalidades da zappaz",
    website_url="https://zappaz.io",
)

mcp.add_middleware(RateLimitMiddleware())
mcp.add_middleware(AuthSessionMiddleware())

mcp.add_tool(send_text_message_tool)
mcp.add_tool(send_image_message_tool)
mcp.add_tool(send_video_message_tool)
mcp.add_tool(send_audio_message_tool)
mcp.add_tool(send_document_message_tool)
mcp.add_tool(send_contact_message_tool)
mcp.add_tool(send_location_message_tool)
mcp.add_tool(delete_message_tool)


if __name__ == "__main__":
    asyncio.run(mcp.run_http_async(port=8001, host="0.0.0.0"))