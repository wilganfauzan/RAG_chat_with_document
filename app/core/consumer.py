import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chats.task import process_chat
from pyexpat.errors import messages


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(
            "notification", self.channel_name
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "notification", self.channel_name
        )

    async def send_notification(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))