import random
from typing import Any, Callable, Dict

from paho.mqtt.client import Client, MQTTMessage

BROKER = "broker.emqx.io"
PORT = 1883
CLIENT_ID = f"python-mqtt-{random.randint(0, 1000)}"
USERNAME = "emqx"
PASSWORD = "public"


class Topics:
    RESPONSE_TEXT = "ResponseText"
    RESPONSE_TEXT_FILE = "ResponseTextFile"
    RESPONSE_FUNC_EVAL = "ResponseFuncEval"
    REQUEST_TEXT = "RequestText"
    REQUEST_TEXT_FILE = "RequestTextFile"
    REQUEST_FUNC_EVAL = "RequestFuncEval"

    @staticmethod
    def request_topics():
        return [
            (Topics.REQUEST_TEXT, 0),
            (Topics.REQUEST_TEXT_FILE, 0),
            (Topics.REQUEST_FUNC_EVAL, 0),
        ]

    @staticmethod
    def response_topics():
        return [
            (Topics.RESPONSE_TEXT, 0),
            (Topics.RESPONSE_TEXT_FILE, 0),
            (Topics.RESPONSE_FUNC_EVAL, 0),
        ]


def mqtt_connect() -> Client:
    def on_connect(client: Client, userdata: Any, flags: Dict[str, int], rc: int):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = Client(CLIENT_ID)
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def mqtt_subscribe(
    client: Client,
    topics: Any,
    on_message: Callable[[Client, Any, MQTTMessage], None],
):
    client.subscribe(topics)
    client.on_message = on_message


def mqtt_publish(client: Client, topic: str, message: str):
    result = client.publish(topic, message)
    if result[0] == 0:
        print(f"Sent `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
