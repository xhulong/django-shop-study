import datetime
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from common import SparkApi


class ChatConsumer(WebsocketConsumer):
    text = []

    def get_text(self, role, content):
        jsoncon = {'role': role, 'content': content}
        self.text.append(jsoncon)
        return self.text

    def getlength(self, text):
        length = 0
        for content in text:
            temp = content["content"]
            leng = len(temp)
            length += leng
        return length

    def checklen(self, text):
        while self.getlength(text) > 8000:
            del text[0]
        return text

    def connect(self):
        self.group = self.scope['url_route']['kwargs']['group']
        self.room_group_name = 'chat_%s' % self.group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
            'message': '连接成功'
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        try:
            message = json.loads(text_data)
        except json.decoder.JSONDecodeError as e:
            # 处理 JSON 解析错误
            print(f"JSON decode error: {e}")
            return

        if 'question' in message:
            self.question = message['question']
            self.id = message['id']
            self.checklen(self.get_text('user', self.question))
            def callback(answer, status):
                self.checklen(self.get_text('user', answer))
                self.send(text_data=json.dumps({
                    'answer': answer,
                    'status': status,
                    'id': self.id
                }))
            SparkApi.main(self.text, callback)