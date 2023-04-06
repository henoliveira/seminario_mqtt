import random

from paho.mqtt import client as MqttClient

BROKER = "broker.emqx.io"
PORT = 1883
CLIENT_ID = f"python-mqtt-{random.randint(0, 1000)}"
USERNAME = "emqx"
PASSWORD = "public"

RESPONSE_TOPICS = [
    ("response_text", 0),
    ("response_text_file", 0),
    ("response_func_eval", 0),
]
REQUEST_TOPICS = [
    ("request_text", 0),
    ("request_text_file", 0),
    ("request_func_eval", 0),
]


def mqtt_connect() -> MqttClient:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = MqttClient.Client(CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def mqtt_subscribe(client: MqttClient, topics, on_message: callable):
    client.subscribe(topics)
    client.on_message = on_message


def mqtt_publish(client: MqttClient, topic: str, message: str):
    result = client.publish(topic, message)
    if result[0] == 0:
        print(f"Send `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
