# mqtt_publisher.py
import paho.mqtt.client as mqtt
import json
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def publish_data(value):
    # MQTT 클라이언트 생성
    client = mqtt.Client()
    client.on_connect = on_connect

    # MQTT 브로커에 연결
    client.connect("test.mosquitto.org", 1883, 60)

    # 메시지 준비
    data = {'value': value}
    payload = json.dumps(data)

    # 메시지 발행
    client.publish("your/mqtt/topic", payload)
    print(f"Published: {payload}")

    # 연결 종료
    client.disconnect()

if __name__ == "__main__":
    while True:
        # 예시 값으로 데이터를 발행
        value = 42  # 여기에서 원하는 값을 설정
        publish_data(value)
        
        # 주기적으로 발행 (예: 5초 간격)
        time.sleep(5)