"""MQTT Protocol."""
import paho.mqtt.client as mqtt
import ssl


def on_connect(mqttc, obj, flags, rc):
    """MQTT on connect callback."""
    print("connected: " + str(rc))


def on_message(mqttc, obj, msg):
    """MQTT on message callback."""
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    """MQTT on publish callback."""
    print("message_id: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    """MQTT on subscribe callback."""
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    """MQTT on log, for debugging, callback."""
    print(string)


def connect(connection_data):
    """MQTT connect."""
    if type(connection_data) is not dict:
        return None

    if "client_id" in connection_data:
        mqtt_client = mqtt.Client(connection_data["client_id"])
    else:
        print ('Cannot connect. Missing "client_id".')
        return None

    mqtt_client.on_connect = on_connect
    mqtt_client.on_publish = on_publish
    mqtt_client.on_subscribe = on_subscribe
    mqtt_client.on_log = on_log

    if "username" in connection_data and\
       "password" in connection_data:
        mqtt_client.username_pw_set(username=connection_data["username"],
                                    password=connection_data["password"])
    elif "ca" in connection_data and\
         "certificate" in connection_data and\
         "private_key" in connection_data:
        mqtt_client.tls_set(connection_data["ca"],
                            certfile=connection_data["certificate"],
                            keyfile=connection_data["private_key"],
                            cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2,
                            ciphers=None)

    print("Trying to connect 1")

    if "endpoint" in connection_data:
        if "port" in connection_data:
            port = connection_data["port"]
        else:
            port = 1883

        if "keepalive" in connection_data:
            keepalive = connection_data["keepalive"]
        else:
            keepalive = 60

        print("Trying to connect 2")
        mqtt_client.connect(host=connection_data["endpoint"],
                            port=port, keepalive=keepalive)
        mqtt_client.loop_start()

        return mqtt_client
    else:
        return None