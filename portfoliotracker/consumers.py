import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

#from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name="checking"
        await self.channel_layer.group_add(self.group_name,self.channel_name)
        await self.accept()
        print("conneccted websockert in django ")

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print("hello disconnected from chat app ")

    async def send_message(self, event):
        message = json.loads(event['message'])

        # Send message to WebSocket
        await self.send(json.dumps(message))






