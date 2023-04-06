import utils


def on_message(c):
    pass


def main():
    client = utils.mqtt_connect()
    # utils.mqtt_subscribe(client, utils.REQUEST_TOPICS, on_message)

    client.loop_start()
    utils.mqtt_publish(client, "request_text", "Hello World!")


if __name__ == "__main__":
    main()
