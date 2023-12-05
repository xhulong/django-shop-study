import datetime
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.exceptions import StopConsumer


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
        while (self.getlength(text) > 8000):
            del text[0]
        return text

    def connect(self):
        # 在建立连接时执行的操作
        # 可以在这里进行认证、建立会话等操作
        print(self.scope['url_route']['kwargs']['group'], '已连接')
        # self.question = self.scope['url_route']['kwargs']['question']
        self.question = "写个五百字的搞笑段子"
        self.group = self.scope['url_route']['kwargs']['group']
        self.room_group_name = 'chat_%s' % self.group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.answer = ""
        self.checklen(self.get_text('user', self.question))
        SparkApi.main(self.text)
        print(SparkApi.answer,'answer')
        self.get_text('assistant', SparkApi.answer)
        datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.send(text_data=json.dumps({
            'message': datetime_str + ' ' + self.group + ' ' + self.question + ' ' + SparkApi.answer
        }))

    def disconnect(self, close_code):
        # 在断开连接时执行的操作
        # 可以在这里进行清理工作、关闭会话等操作
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):   # 接收到消息时执行的操作
        print(text_data)
        # text_data_json = json.loads(text_data)
        message = text_data

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):  # 从room group中接收到消息时执行的操作
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
