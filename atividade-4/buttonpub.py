########################################################
# Topicos Avancados em Redes de Computadores - Grupo 9
#######################################################
#
# Programa publisher para button On e Off para os leds   
# CAIO HENRIQUE GIACOMELLI
# RAFAEL PEREIRA ALONSO
# RICARDO MENDES LEAL JUNIOR 
# ROBSON MIRIM DO CARMO


# Atividade 4 -> Publica Button ON OFF
#######################################################
#!/usr/bin/python3

# imports
from libsoc_zero.GPIO import Button
from time import sleep
import paho.mqtt.client as mqtt
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')

ip_broker = "localhost"  

qos = 0
topico = "digital"
no_connection_message = "*** Sem Conexao ***"

print("#########################################")
print("Atividade-4 - Sensor de toque + Led")
print("#########################################")
print ("\nIniciando Aplicacao !!!")

def on_disconnect(client, userdata, rc):
    print("\n*** Queda de conexao ***")


client = mqtt.Client()
 
client.will_set(topico, no_connection_message, 0, True)

print("\nStarting subscriber...")
client.on_disconnect = on_disconnect   

client.connect(ip_broker)

client.loop_start()
print("\nStarting publisher...")
btn = Button('GPIO-A')

#####################
# rotina principal  #   
#####################
ledOn=0
ledstatus=""
while True:
    sleep(0.3)
    if btn.is_pressed():
        if ledOn==0:
            ledOn = 1
            ledstatus="ON"
        else :
            ledOn = 0    
            ledstatus="OFF"
        pub = client.publish("digital", ledstatus)
