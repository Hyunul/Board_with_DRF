import sys
import os

# DJANGO_SETTINGS_MODULE 환경 변수 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_prac.settings')  # 프로젝트 이름 확인

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import django
django.setup()

import paho.mqtt.client as mqtt
from models import DataPoint
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

def on_connect(client, userdata, flags, rc):
    client.subscribe("selimcns/status")
    print("success")

def on_message(client, userdata, msg):
    data = json.loads(msg.payload)
    print(data)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("qideun.com", 1883, 60)
client.loop_start()