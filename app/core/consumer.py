import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("notification", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notification", self.channel_name)

    async def send_notification(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.document_id = self.scope["url_route"]["kwargs"]["document_id"]
        self.group_name = f"chat_{self.document_id}"

        await self.accept()
        await self.channel_layer.group_add("chat", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chat", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"] ##Message received from client or frontend

        print(f"Message received: {message}")

    async def send_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps({"message": message}))
