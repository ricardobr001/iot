#coding: utf-8

from libsoc_zero.GPIO import Button
from time import sleep
import paho.mqtt.client as mqtt
#import time

# This is the Publisher

# Cria cliente mqtt
client = mqtt.Client()

# Cria o testamento para o topico "topic/9", mensagem = "Desconectando..". QOS = 1

# Conecta o cliente ao Broker fornecido em aula
client.connect("192.168.123.17",1883,60)

# Publica a mensagem "Conectado" no topico "topic/AULA", com o QOS = 0
client.publish("topic/grupo9", "Conectado", 2)

btn1 = Button('GPIO-A')

while True:
    sleep(0.25)
    if btn1.is_pressed():
        client.publish("topic/grupo9", "1")
    else:
        client.publish("topic/grupo9", "0")
