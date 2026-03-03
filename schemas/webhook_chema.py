from pydantic import BaseModel, Field
from typing import Optional

class WebhookEvents(BaseModel):
    call: bool = False
    blocklist_set: Optional[bool] = Field(default=False, alias="blocklist.set")
    blocklist_update: Optional[bool] = Field(default=False, alias="blocklist.update")
    chats_delete: Optional[bool] = Field(default=False, alias="chats.delete")
    chats_phoneNumberShare: Optional[bool] = Field(default=False, alias="chats.phoneNumberShare")
    chats_update: Optional[bool] = Field(default=False, alias="chats.update")
    chats_upsert: Optional[bool] = Field(default=False, alias="chats.upsert")
    connection_update: Optional[bool] = Field(default=False, alias="connection.update")
    contacts_update: Optional[bool] = Field(default=False, alias="contacts.update")
    contacts_upsert: Optional[bool] = Field(default=False, alias="contacts.upsert")
    creds_update: Optional[bool] = Field(default=False, alias="creds.update")
    group_participants_update: Optional[bool] = Field(
        default=False, alias="group-participants.update"
    )
    group_join_request: Optional[bool] = Field(default=False, alias="group.join-request")
    groups_update: Optional[bool] = Field(default=False, alias="groups.update")
    groups_upsert: Optional[bool] = Field(default=False, alias="groups.upsert")
    labels_association: Optional[bool] = Field(default=False, alias="labels.association")
    labels_edit: Optional[bool] = Field(default=False, alias="labels.edit")
    message_receipt_update: Optional[bool] = Field(
        default=False, alias="message-receipt.update"
    )
    messages_delete: Optional[bool] = Field(default=False, alias="messages.delete")
    messages_media_update: Optional[bool] = Field(
        default=False, alias="messages.media-update"
    )
    messages_reaction: Optional[bool] = Field(default=False, alias="messages.reaction")
    messages_send: Optional[bool] = Field(default=False, alias="messages.send")
    messages_update: Optional[bool] = Field(default=False, alias="messages.update")
    messaging_history_set: Optional[bool] = Field(
        default=False, alias="messaging-history.set"
    )
    presence_update: Optional[bool] = Field(default=False, alias="presence.update")
    inbound_message_upsert: Optional[bool] = Field(
        default=False, alias="inbound-message.upsert"
    )
    outbound_message_upsert: Optional[bool] = Field(
        default=False, alias="outbound-message.upsert"
    )

class WebookHeader(BaseModel):
    Authorization: str


class Webhook(BaseModel):
    url: str
    displayName: str
    enabled: bool
    events: WebhookEvents
    headers: Optional[WebookHeader] = None