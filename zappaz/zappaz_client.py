from httpx import AsyncClient

client = AsyncClient(
    base_url='https://api.zappaz.io/api/v1',
    timeout=30.0
)

def get_headers(token: str):
    return {"Authorization": token, "Content-Type": "application/json"}
