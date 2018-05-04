#coding: utf-8

import paho.mqtt.client as mqtt
from libsoc_zero.GPIO import LED

led = LED('GPIO-C')

# The callback for when the client receives a CONNACK response from the server.
# O callback de quando o cliente recebe uma resposta CONACK do servidor
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("topic/grupo9")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if str(msg.payload) == "b\'1\'":
         print ('\rBotão pressionado    ', end='')
         led.on()
    else:
         print ('\rBotão não pressionado', end='')
         led.off()

client = mqtt.Client()

# Overwrite the methods on_connect and on_message from paho.mqtt.client
client.on_connect = on_connect
client.on_message = on_message

# Connecting to the server and looping forever
client.connect("192.168.123.17", 1883, 60)
client.loop_forever()
