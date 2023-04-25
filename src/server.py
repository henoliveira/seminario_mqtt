from typing import Any

import utils as utils


def response_text(
    client: utils.Client,
    payload: str,
    topic_req: str,
    topic_res: str,
):
    print(f"Got `{payload}` from topic `{topic_req}`")
    utils.mqtt_publish(client, topic_res, payload.upper())


def reponse_text_file(
    client: utils.Client,
    payload: str,
    topic_req: str,
    topic_res: str,
):
    arquivo = open("file.txt", "w")
    arquivo.write(payload)
    arquivo.close()
    print(f"Got `{payload}` from topic `{topic_req}`")
    utils.mqtt_publish(client, topic_res, "File edited successfully!")


def reponse_func_eval(
    client: utils.Client,
    payload: str,
    topic_req: str,
    topic_res: str,
) -> None:
    print(f"Got `{payload}` from topic `{topic_req}`")
    utils.mqtt_publish(client=client, topic=topic_res, message=str(eval(payload)))


def on_message(client: utils.Client, userdata: Any, message: utils.MQTTMessage) -> None:
    topic = message.topic
    payload = message.payload.decode()

    if topic == utils.Topics.REQUEST_TEXT:
        response_text(client, payload, topic, utils.Topics.RESPONSE_TEXT)

    elif topic == utils.Topics.REQUEST_TEXT_FILE:
        reponse_text_file(client, payload, topic, utils.Topics.RESPONSE_TEXT_FILE)

    elif topic == utils.Topics.REQUEST_FUNC_EVAL:
        reponse_func_eval(client, payload, topic, utils.Topics.RESPONSE_FUNC_EVAL)


def main():
    client = utils.mqtt_connect()
    utils.mqtt_subscribe(client, utils.Topics.request_topics(), on_message)
    client.loop_forever()


if __name__ == "__main__":
    main()
