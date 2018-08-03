# -*- coding: utf-8 -*-

import os
import logging
import api.mqtt as mqtt
import subprocess
from time import sleep
from api.twitter import Twitter
from api.ubidots import post_request
from subprocess import Popen, PIPE
from weather import Weather, Unit

''' 
    Valores TOKEN e DEVICE_LABEL
    Para poder enviar os dados para a nuvem
'''
TOKEN = "BBFF-m1tW3P8lTsfrogcltXCkXY0dDDfb9b"
DEVICE_LABEL = "teste"


'''
    Compilando os arquivos .c para recuperar o valor das entradas analógicas
'''
subprocess.call("gcc analog1_temp.c  -lsoc -o temp",   shell=True)
subprocess.call("gcc analog2_light.c -lsoc -o light",  shell=True)
subprocess.call("gcc port1_slider.c  -lsoc -o slider", shell=True)
subprocess.call("gcc port2_tilt.c    -lsoc -o tilt",   shell=True)
subprocess.call("gcc port3_button.c  -lsoc -o button", shell=True)
logging.getLogger("requests").setLevel(logging.WARNING)


'''
    Conexão do MQTT
'''

ip_broker = "localhost"  
qos = 0
topic = "teste"
no_connection_message = "Publisher desconectado\n"

client = mqtt.Client()
client.will_set(topic, no_connection_message, 0, True)
client.connect(ip_broker)
client.publish(topic, "Publisher conectado", qos)

######### API OBJECT CREATION ######### 
'''
    API do Twitter. Parametros:
        1 - texto que sera procurado pela API
        2 - Palavra de emergencia, caso encontrada devera enviar uma mensagem
        3 - Tempo de diferença entre os tweets para enviar a mensagem em SEGUNDOS
        4 - Quantidade de tweets necessários para enviar a mensagem
'''

# t = Twitter('#neymar', 'se jogou', 30, 6)



'''
     Essa API verifica a temperatura em (http://weather.yahoo.com)
'''
weather = Weather(unit=Unit.CELSIUS) # Inicializando o novo objeto


################ MAIN PROCESS #################
try:
    while(True):
        # clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        print("######################")
        print("# Valor dos sensores #")
        print("######################\n")

        ################################################
        #################    TILT    ###################
        tilt        = Popen(["./tilt"],   stdout=PIPE)
        ti          = tilt.stdout.read()
        tiltValue   = str(ti.decode()).split('\n')[0]
        print("tilt: "      + tiltValue)
        ################################################

        ################################################
        ################# TEMPERATURA ##################
        #################   SENSOR  ####################
        temp        = Popen(["./temp"],   stdout=PIPE)
        te          = temp.stdout.read()
        tempValue   = str(te.decode()).split('\n')[0]
        print("temp sens: " + tempValue   + "C")
        #################    REAL   ####################
        # local         = weather.lookup_by_location('sorocaba') 
        # temperatura = local.condition.temp
        temperatura = "20"
        print("temp real: " + temperatura + "C")
        ################################################

        ################################################
        #################     LUZ     ##################
        light       = Popen(["./light"],  stdout=PIPE)
        li          = light.stdout.read()
        lightValue  = str(li.decode()).split('\n')[0]
        print("light: "     + lightValue)
        ################################################

        ################################################
        #################    BUTTON   ##################
        button      = Popen(["./button"], stdout=PIPE)
        bt          = button.stdout.read()
        buttonValue = str(bt.decode()).split('\n')[0]
        print("Button: "    + buttonValue)
        ################################################
        
        ################################################
        #################   TWITTER   ##################
        # if t.busca():
        #   twitterValue = True
        # else:
        #   twitterValue = False
        twitterValue = True
        ################################################
        
        ################################################
        #################  PUBLISHER  ##################
        message = ""
        if (int(tiltValue) == 1):
            message += "Tremores detectados!\n"
        if (float(tempValue) > int(temperatura) + 5):
            message += "Temperatura muito elevada!!\n"
        if (int(lightValue) > 900):
            message += "Nivel de luminosidade alta!!!\n"
        if (int(buttonValue) == 1):
            message += "BOTAO DE EMERGENCIA PRESSIONADO!!!!\n"
        if (twitterValue):
            message += "EMERGENCIA!!!!!\n"
        if (message == ""):
            client.publish(topic, "Nenhuma anomalia detectada", qos)
        else:
            client.publish(topic, message, qos)
        ################################################

        ################################################
        # two seconds sleep
        print("\n######################")
        sleep(2)
        ################################################
except KeyboardInterrupt:
    pass
else:
    mqtt_client.disconnect()
sys.exit(0)


'''
    ################################################
    #################    SLIDER   ##################
    slider      = Popen(["./slider"], stdout=PIPE)
    sl          = slider.stdout.read()
    sliderValue = str(sl.decode()).split('\n')[0]
    print("slider: "    + sliderValue)
    ################################################
'''