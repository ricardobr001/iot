########################################################
# Topicos Avancados em Redes de Computadores - Grupo 9
#######################################################
#
# Programa publisher para button On e Off para os leds   

# CAIO HENRIQUE GIACOMELLI
# RAFAEL PEREIRA ALONSO
# RICARDO MENDES LEAL JUNIOR 
# ROBSON MIRIM DO CARMO

# Atividade 4 -> Consome fila apos button pub (Led On Led Off
#######################################################
#!/usr/bin/python3

# Imports
from libsoc_zero.GPIO import Button
from libsoc_zero.GPIO import LED
from time import sleep
import paho.mqtt.client as mqtt
import os
import sys
from time import sleep

# limpa o console a cada execução  
os.system('cls' if os.name == 'nt' else 'clear')

ip_broker = "localhost"
 
topico = "digital"
ledstatus = LED('GPIO-C')

print("#####################################")
print("# Consome led off e on ............ #")
print("#.................................. #")
print("# OFF Openhab = '0' sensor de toque #")
print("#.................................. #")
print("# ON  Openhab = '1' sensor de toque #")
print("#...................................#")

########################################
# Detalhe da rotina de consumo On Off
########################################
def on_message(client, userdata, msg):
    if msg.payload.decode('utf8','strict') == "OFF" :
        ledstatus.off() 
        print("\nConsumo led status OFF ==>: " + msg.payload.decode('utf8','strict'))
    else:
        ledstatus.on()
        print("\nConsumo led status ON ===>: " + msg.payload.decode('utf8','strict'))
    sleep (1.7)

client = mqtt.Client()
client.connect(ip_broker)
client.on_message = on_message
client.subscribe(topico, 0)

print("Starting subscriber...")
client.loop_forever()
