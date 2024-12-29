from django.urls import path
from . import consumers  # 소비자 가져오기

websocket_urlpatterns = [
    path('ws/chart_updates/', consumers.ChartUpdateConsumer.as_asgi()),  # WebSocket URL
]