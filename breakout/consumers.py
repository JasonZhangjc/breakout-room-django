from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync, sync_to_async
from .models import BreakoutModel

# class BreakoutConsumer(WebsocketConsumer):

#     def connect(self):
#         # a layer is to be created
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'breakout_'+str(self.room_name)
#         async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
#         self.accept()

#     def disconnect(self):
#         # The layer is to be deleted
#         async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         async_to_sync(self.channel_layer.group_send)(self.room_group_name, {'message': message, 'type':'send_back'})

#     def send_back(self, event):
#         message = event['message']
#         self.send(text_data=json.dumps({'message': message}))


class BreakoutConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # a layer is to be created
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'breakout_'+str(self.room_name)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self):
        # The layer is to be deleted
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await sync_to_async(BreakoutModel(room_number = self.room_name, message=message).save)()
        await self.channel_layer.group_send(self.room_group_name, {'message': message, 'type':'send_back'})

    async def send_back(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))