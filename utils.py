import random
import time

from paho.mqtt import client as mqtt_client

import utils

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = [("text_response", 0), ("text_file", 0), ("func_eval", 0)]
CLIENT_ID = f"python-mqtt-{random.randint(0, 1000)}"
USERNAME = "emqx"
PASSWORD = "public"


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def publish(client: mqtt_client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(utils.TOPIC, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{utils.TOPIC}`")
        else:
            print(f"Failed to send message to topic {utils.TOPIC}")
        msg_count += 1


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(utils.TOPIC)
    client.on_message = on_message
