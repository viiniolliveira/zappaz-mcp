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

from tools.group_tool import (
    list_groups_tool,
    get_group_participants_tool,
    create_group_tool,
    remove_participants_tool,
    add_participants_tool,
    promote_participants_tool,
    demote_participants_tool,
    send_group_invite_link_tool,
    update_group_tool,
    update_group_picture_tool
)

from tools.webhook_tool import (
    create_webhook_tool,
    delete_webhook_tool,
    get_webhooks_tool,
    update_webhook_tool
)

mcp = FastMCP(
    name="Zappaz MCP",
    instructions="Este é um mcp server da zappaz api uma api de WhatsApp, que da acesso a todas as funcionalidades da zappaz",
    website_url="https://zappaz.io",
)

mcp.add_middleware(RateLimitMiddleware())
mcp.add_middleware(AuthSessionMiddleware())

# Message tools
mcp.add_tool(send_text_message_tool)
mcp.add_tool(send_image_message_tool)
mcp.add_tool(send_video_message_tool)
mcp.add_tool(send_audio_message_tool)
mcp.add_tool(send_document_message_tool)
mcp.add_tool(send_contact_message_tool)
mcp.add_tool(send_location_message_tool)
mcp.add_tool(delete_message_tool)

# Group tools
mcp.add_tool(list_groups_tool)
mcp.add_tool(get_group_participants_tool)
mcp.add_tool(create_group_tool)
mcp.add_tool(remove_participants_tool)
mcp.add_tool(add_participants_tool)
mcp.add_tool(promote_participants_tool)
mcp.add_tool(demote_participants_tool)
mcp.add_tool(send_group_invite_link_tool)
mcp.add_tool(update_group_tool)
mcp.add_tool(update_group_picture_tool)

# Webhook tools
mcp.add_tool(get_webhooks_tool)
mcp.add_tool(create_webhook_tool)
mcp.add_tool(update_webhook_tool)
mcp.add_tool(delete_webhook_tool)

if __name__ == "__main__":
    asyncio.run(mcp.run_http_async(port=8001, host="0.0.0.0"))