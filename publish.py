from paho.mqtt import client as mqtt_client

import utils


def publish(client: mqtt_client, message: str):
    topic = "text_response"
    result = client.publish(topic, message)
    if result[0] == 0:
        print(f"Send `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def run():
    client = utils.connect_mqtt()
    client.loop_start()
    publish(client, "Hello World!")


if __name__ == "__main__":
    run()
