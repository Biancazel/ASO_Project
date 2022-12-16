import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message
import datetime


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.roomGroupName = "group_chat_gfg"
        async_to_sync(self.channel_layer.group_add)(
            self.roomGroupName,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.roomGroupName,
            self.channel_layer
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        is_writing_data = text_data_json["is_writing_data"]
        image = text_data_json["image"]
        if image is not None:
            msg = Message(content=image, owner=username, timestamp=datetime.datetime.now(), is_image=1)
            msg.save()
        else:
            msg = Message(content=message, owner=username, timestamp=datetime.datetime.now())
            if not is_writing_data:
                msg.save()

        async_to_sync(self.channel_layer.group_send)(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
                "is_writing_data": is_writing_data,
                "image": image
            }
        )

    def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        is_writing_data = event["is_writing_data"]
        image = event["image"]
        async_to_sync(self.send(text_data=json.dumps(
            {"message": message, "username": username, "is_writing_data": is_writing_data, "image": image})))
