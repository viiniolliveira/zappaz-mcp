from pydantic import BaseModel, Field
from typing import List, Optional

class TextMessage(BaseModel):
    number: str = Field(..., description="Número do remetente da mensagem")
    message: str = Field(..., description="Conteúdo da mensagem")
    mentions: Optional[List[str]] = Field(default_factory=list, description="Lista de números mencionados na mensagem, use uma lista vazia para não mencionar ninguém.")
    quoted: Optional[str] = Field(default_factory=str, description="ID da mensagem citada, se houver, para enviar como resposta. Use uma string vazia para não citar nenhuma mensagem.")
    delay: Optional[int] = Field(0, description="Tempo de atraso para resposta em milissegundos")
    linkPreview: Optional[bool] = Field(True, description="Indica se a mensagem é uma pré-visualização de link")


class ImageMessage(BaseModel):
    number: str = Field(..., description="Número do remetente da mensagem")
    source: str = Field(..., description="URL ou Base64 da imagem a ser enviada")
    caption: Optional[str] = Field(None, description="Legenda para a imagem")
    fileName: Optional[str] = Field(None, description="Nome do arquivo da imagem")
    mentions: Optional[List[str]] = Field(default_factory=list, description="Lista de números mencionados na mensagem, use uma lista vazia para não mencionar ninguém.")
    quoted: Optional[str] = Field(default_factory=str, description="ID da mensagem citada, se houver, para enviar como resposta. Use uma string vazia para não citar nenhuma mensagem.")
    delay: Optional[int] = Field(0, description="Tempo de atraso para resposta em milissegundos")


class VideoMessage(BaseModel):
    number: str = Field(..., description="Número do remetente da mensagem")
    source: str = Field(..., description="URL ou Base64 do vídeo a ser enviado")
    caption: Optional[str] = Field(None, description="Legenda para o vídeo")
    fileName: Optional[str] = Field(None, description="Nome do arquivo do vídeo")
    mentions: Optional[List[str]] = Field(default_factory=list, description="Lista de números mencionados na mensagem, use uma lista vazia para não mencionar ninguém.")
    quoted: Optional[str] = Field(default_factory=str, description="ID da mensagem citada, se houver, para enviar como resposta. Use uma string vazia para não citar nenhuma mensagem.")
    delay: Optional[int] = Field(0, description="Tempo de atraso para resposta em milissegundos")


class AudioMessage(BaseModel):
    number: str = Field(..., description="Número do remetente da mensagem")
    source: str = Field(..., description="URL ou Base64 do áudio a ser enviado")
    mentions: Optional[List[str]] = Field(default_factory=list, description="Lista de números mencionados na mensagem, use uma lista vazia para não mencionar ninguém.")
    quoted: Optional[str] = Field(default_factory=str, description="ID da mensagem citada, se houver, para enviar como resposta. Use uma string vazia para não citar nenhuma mensagem.")
    delay: Optional[int] = Field(0, description="Tempo de atraso para resposta em milissegundos")


class DocumentMessage(BaseModel):
    number: str = Field(..., description="Número do remetente da mensagem")
    source: str = Field(..., description="URL ou Base64 do documento a ser enviado")
    caption: Optional[str] = Field(None, description="Legenda para o documento")
    fileName: Optional[str] = Field(None, description="Nome do arquivo do documento")
    mentions: Optional[List[str]] = Field(default_factory=list, description="Lista de números mencionados na mensagem, use uma lista vazia para não mencionar ninguém.")
    quoted: Optional[str] = Field(default_factory=str, description="ID da mensagem citada, se houver, para enviar como resposta. Use uma string vazia para não citar nenhuma mensagem.")
    delay: Optional[int] = Field(0, description="Tempo de atraso para resposta em milissegundos")


class Contact(BaseModel):
    phoneNumber: str = Field(..., description="Número do contato")
    firstName: Optional[str] = Field(None, description="Primeiro nome do contato")
    lastName: Optional[str] = Field(None, description="Último nome do contato")

class ContactMessage(BaseModel):
    number: str = Field(..., description="Número do remetente da mensagem")
    contact: Contact = Field(..., description="Contato a ser enviado")
    delay: Optional[int] = Field(0, description="Tempo de atraso para resposta em milissegundos")



class Location(BaseModel):
    latitude: Optional[float] = Field(None, description="Latitude da localização")
    longitude: Optional[float] = Field(None, description="Longitude da localização")
    address: Optional[str] = Field(None, description="Endereço da localização")
    name: Optional[str] = Field(None, description="Nome do local")
    url: Optional[str] = Field(None, description="URL associada à localização")
    comment: Optional[str] = Field(None, description="Comentário sobre a localização")

class LocationMessage(BaseModel):
    number: str = Field(..., description="Número do remetente da mensagem")
    location: Location = Field(..., description="Localização a ser enviada")