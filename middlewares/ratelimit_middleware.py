import time
from collections import defaultdict, deque

from fastmcp.server.middleware import Middleware, MiddlewareContext
from fastmcp.server.dependencies import get_http_request
from fastmcp.exceptions import McpError
from mcp.types import ErrorData

class RateLimitMiddleware(Middleware):
    def __init__(self, limit: int = 5, window_seconds: int = 1, max_keys: int = 1000):
        self.limit = limit
        self.window = window_seconds
        self.max_keys = max_keys
        self._buckets: dict[str, deque[float]] = defaultdict(deque)

    async def on_request(self, context: MiddlewareContext, call_next):
        request = get_http_request()
        if not request:
            return await call_next(context)

        if len(self._buckets) > self.max_keys:
            self._buckets.clear()

        # chave do rate limit: sessionId (se existir) senão IP
        session_id = request.query_params.get("sessionId")
        ip = request.client.host if request.client else "unknown"
        key = f"sid:{session_id}" if session_id else f"ip:{ip}"

        now = time.time()
        bucket = self._buckets[key]

        # remove timestamps fora da janela
        cutoff = now - self.window
        while bucket and bucket[0] <= cutoff:
            bucket.popleft()

        if len(bucket) >= self.limit:
            raise McpError(ErrorData(message="Rate limit exceeded", code=429))

        bucket.append(now)

        return await call_next(context)