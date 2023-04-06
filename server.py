import utils


def response_text(
    client: utils.MqttClient,
    payload: str,
    topic_req: str,
    topic_res: str,
):
    response = f"RESPONSE TO: Received `{payload}` from `{topic_req}` topic"
    print(f"Received `{payload}` from `{topic_req}` topic")
    utils.mqtt_publish(client, topic_res, payload)
    print(f"Sent `{response}` to `{topic_res}` topic")


def reponse_text_file(
    client: utils.MqttClient,
    payload: str,
    topic_res: str,
):
    print(f"Received `{payload}` from `{topic_res}` topic")


def reponse_func_eval(
    client: utils.MqttClient,
    payload: str,
    topic_res: str,
):
    try:
        result = eval(payload)
        utils.mqtt_publish(client, str(result))
        print(f"Received `{result}` from `{topic_res}` topic")
    except Exception as e:
        print(f"Failed to evaluate `{payload}` from `{topic_res}` topic: {e}")


def on_message(client, userdata, message: str):
    topic = message.topic
    payload = message.payload.decode()

    match topic:
        case "request_text":
            response_text(client, payload, topic, "response_text")
        case "request_text_file":
            reponse_text_file(client, topic, payload)
        case "request_func_eval":
            reponse_func_eval(client, payload, topic)


def main():
    client = utils.mqtt_connect()
    utils.mqtt_subscribe(client, utils.REQUEST_TOPICS, on_message)
    client.loop_forever()


if __name__ == "__main__":
    main()
