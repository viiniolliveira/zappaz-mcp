from schemas.message_schema import *
from zappaz.zappaz_client import client, get_headers


async def send_text_message(data: TextMessage, sessionId: str, token: str):
        headers = get_headers(token)
        response = await client.post(
            url=f"/session/{sessionId}/message/text", 
            json=data.model_dump(), 
            headers=headers
            )
        return response.json()


async def send_image_message(data: ImageMessage, sessionId: str, token: str):
        headers = get_headers(token)
        response = await client.post(
            url=f"/session/{sessionId}/message/image", 
            json=data.model_dump(), 
            headers=headers
            )
        return response.json()


async def send_video_message(data: VideoMessage, sessionId: str, token: str):
        headers = get_headers(token)
        response = await client.post(
            url=f"/session/{sessionId}/message/video", 
            json=data.model_dump(), 
            headers=headers
            )
        return response.json()


async def send_audio_message(data: AudioMessage, sessionId: str, token: str):
        headers = get_headers(token)
        response = await client.post(
            url=f"/session/{sessionId}/message/audio", 
            json=data.model_dump(), 
            headers=headers
            )
        return response.json()


async def send_document_message(data: DocumentMessage, sessionId: str, token: str):
        headers = get_headers(token)
        response = await client.post(
            url=f"/session/{sessionId}/message/document", 
            json=data.model_dump(), 
            headers=headers
            )
        return response.json()


async def send_contact_message(data: ContactMessage, sessionId: str, token: str):
        headers = get_headers(token)
        response = await client.post(
            url=f"/session/{sessionId}/message/contact", 
            json=data.model_dump(), 
            headers=headers
            )
        return response.json()


async def send_location_message(data: LocationMessage, sessionId: str, token: str):
        headers = get_headers(token)
        response = await client.post(
            url=f"/session/{sessionId}/message/location", 
            json=data.model_dump(), 
            headers=headers
            )
        return response.json()


async def delete_message(messageId: str, sessionId: str, token: str):
        headers = get_headers(token)
        response = await client.delete(
            url=f"/session/{sessionId}/message/{messageId}", 
            headers=headers
            )
        return response.json()