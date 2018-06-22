########################################################
# Topicos Avancados em Redes de Computadores - Grupo 9
#######################################################
#
# Programa publisher para eventos de sensor temp tilt    
# ROBSON MIRIM DO CARMO
# Atividade 5 -> Exercicio 3           
# Leitura para o IBM Watson IOT 
# Device: sensor_temp_devid        
#######################################################

import mqtt
import json
import sys
import temp_reader
import tilt_reader

from time import sleep

ORG_ID = "agstig"
DEVICE_ID = "sensor_devtype"
PASSWORD = "piracicaba"
DEVICE_TYPE = "sensors_devid"

CLIENT_ID_FORMAT = "d:{org_id}:{type_id}:{device_id}"
USERNAME = "use-token-auth"
ENDPOINT_FORMAT = "{org_id}.messaging.internetofthings.ibmcloud.com"
EVENT_TOPIC_FORMAT = "iot-2/evt/{event_id}/fmt/json"
COMMAND_TOPIC_FORMAT = "iot-2/cmd/{command_id}/fmt/json"

print("############################################")
print("Atividade-5 - Sensor de temperatura e tilt #")
print("############################################")
print ("\nIniciando Aplicacao !!!")
#

if __name__ == '__main__':
    client_id = CLIENT_ID_FORMAT.format(org_id=ORG_ID, type_id=DEVICE_TYPE,
                                        device_id=DEVICE_ID)
    endpoint = ENDPOINT_FORMAT.format(org_id=ORG_ID)

    connection_data = {}
    connection_data["client_id"] = client_id
    connection_data["endpoint"] = endpoint
    connection_data["username"] = USERNAME
    connection_data["password"] = PASSWORD

    mqtt_client = mqtt.connect(connection_data)
    try:
        while True:
            event_topic = EVENT_TOPIC_FORMAT.format(event_id="tevt")
            # Temperature
            temp = temp_reader.get()
            data = json.dumps({"d": {"temperature": temp}})
            print("publishing: %s" % data)
            (rc, mid) = mqtt_client.publish(event_topic, data, qos=2)

            # Tilt
            t = tilt_reader.get()
            if t == 1:
                data = json.dumps({"d": {"tilt": "tilt Conectado"}})
                print("publishing: tilted")
            else:
                data = json.dumps({"d": {"tilt": "tilt normal"}})
                print("publishing: normal")

            (rc, mid) = mqtt_client.publish(event_topic, data, qos=2)

            sleep(5)

    except KeyboardInterrupt:
        pass
    else:
        mqtt_client.disconnect()
    sys.exit(0)

