from paho.mqtt import client as mqtt_client

import utils


def text_response(topic: str, payload: str):
    print(f"Received `{payload}` from `{topic}` topic")


def text_file(topic: str, payload: str):
    print(f"Received `{payload}` from `{topic}` topic")


def func_eval(topic: str, payload: str):
    print(f"Received `{payload}` from `{topic}` topic")


def on_message(client, userdata, message: str):
    topic = message.topic
    payload = message.payload.decode()

    match topic:
        case "text_response":
            text_response(topic, payload)
        case "text_file":
            text_file(topic, payload)
        case "func_eval":
            func_eval(topic, payload)


def subscribe(client: mqtt_client):
    client.subscribe(utils.TOPIC)
    client.on_message = on_message


def run():
    client = utils.connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == "__main__":
    run()
