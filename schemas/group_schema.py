from pydantic import BaseModel, Field, RootModel
from typing import List, Optional


class CreateGroup(BaseModel):
    subject: str = Field(..., description="Nome do grupo a ser criado")
    description: Optional[str] = Field(None, description="Descrição do grupo")
    participants: List[str] = Field(..., description="Lista de números dos participantes a serem adicionados ao grupo")

class PhoneList(RootModel[List[str]]):
    pass


class InviteLink(BaseModel):
    number: str = Field(..., description="Numero da pessoa para quem o link de convite será enviado")
    message: Optional[str] = Field(None, description="Mensagem personalizada a ser enviada junto com o link de convite")


class UpdateGroup(BaseModel):
    subject: Optional[str] = Field(default_factory=str, description="Novo nome do grupo, use uma string vazia para não alterar o nome")
    description: Optional[str] = Field(default_factory=str, description="Nova descrição do grupo, use uma string vazia para não alterar a descrição")
    onlyAdminsCanPost: Optional[bool] = Field(False, description="Define se apenas administradores podem enviar mensagens no grupo")
    onlyAdminsCanEditInfo: Optional[bool] = Field(True, description="Define se apenas administradores podem editar as informações do grupo")


class UpdateGroupPicture(BaseModel):
    identifier: str = Field(..., description="ID do grupo a ser atualizado a foto")
    source: str = Field(..., description="URL ou Base64 da nova imagem do grupo a ser atualizada")