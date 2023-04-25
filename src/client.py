from time import sleep
from typing import Any

import utils as utils


def on_message(client: utils.Client, userdata: Any, message: utils.MQTTMessage):
    topic = message.topic
    payload = message.payload.decode()
    print(f"Got `{payload}` from topic `{topic}`")


def main():
    client = utils.mqtt_connect()
    utils.mqtt_subscribe(client, utils.Topics().response_topics(), on_message)

    client.loop_start()
    while True:
        sleep(1)
        print()
        print("1. Send text")
        print("2. Send text to edit file")
        print("3. Send function to evaluate")
        print("4. Exit")
        option = input("Choose an option: ")

        if option == "1":
            message = input("Enter message to send: ")
            print()
            utils.mqtt_publish(client, utils.Topics.REQUEST_TEXT, message)
        elif option == "2":
            message = input("Enter message to send to file: ")
            print()
            utils.mqtt_publish(client, utils.Topics.REQUEST_TEXT_FILE, message)
        elif option == "3":
            message = input("Enter function to evaluate: ")
            print()
            utils.mqtt_publish(client, utils.Topics.REQUEST_FUNC_EVAL, message)
        elif option == "4":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
