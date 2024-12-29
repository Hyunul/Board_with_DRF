# your_app_name/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChartUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("chart_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("chart_updates", self.channel_name)

    async def send_chart_update(self, event):
        data = event['data']
        await self.send(text_data=json.dumps(data))