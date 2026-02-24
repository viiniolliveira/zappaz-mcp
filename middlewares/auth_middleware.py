# middleware.py
from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp.server.dependencies import get_http_request
from fastmcp.exceptions import McpError
from mcp.types import ErrorData


class AuthSessionMiddleware(Middleware):
    async def on_request(self, context: MiddlewareContext, call_next):
        request = get_http_request()

        auth = request.headers.get("authorization") if request else None
        session_id = request.query_params.get("sessionId") if request else None

        if not session_id:
            raise McpError(ErrorData(message="Sem sessionId na query", code=400))

        if not auth:
            raise McpError(ErrorData(message="Sem Authorization header", code=401))

        # Armazena no context pra tools usarem
        if context.fastmcp_context:
            await context.fastmcp_context.set_state("session_id", session_id)
            await context.fastmcp_context.set_state("session_token", auth, serializable=False)
    
        return await call_next(context)

