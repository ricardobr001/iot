########################################################
# Topicos Avancados em Redes de Computadores - Grupo 9
#######################################################
#
# Programa publisher para Slider                         

# CAIO HENRIQUE GIACOMELLI
# RAFAEL PEREIRA ALONSO
# RICARDO MENDES LEAL JUNIOR 
# ROBSON MIRIM DO CARMO

# Atividade 4 -> Publica Slider valores
#######################################################
#!/usr/bin/python3

# Imports
import os
from time import sleep
import paho.mqtt.client as mqtt
import spidev
from libsoc import gpio

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=10000
spi.mode = 0b00
spi.bits_per_word = 8
channel_select=[0x01, 0x80, 0x00]

ip_broker = "localhost"  
qos = 0

###########################################
# Define topico analogido para o "slider"
###########################################

topico = "analog"
print("#########################################")
print("# Atividade-4 - Sensor Analogico Slider #")
print("#########################################")
print ("\nIniciando Aplicacao !!!")

client = mqtt.Client()
client.connect(ip_broker)
gpio_cs = gpio.GPIO(18, gpio.DIRECTION_OUTPUT)

with gpio.request_gpios([gpio_cs]):
    while True:
        gpio_cs.set_high()
        gpio_cs.set_low()
        rx = spi.xfer(channel_select)
        gpio_cs.set_high()
           
        adc_value = (rx[1] << 8) & 0b1100000000
        adc_value = adc_value | (rx[2] & 0xff)
        print("Valor Atual do Slider: %2.1f\n" % ((adc_value /1024) * 100) )
        pub = client.publish(topico, ((adc_value /1024) * 100) )
        sleep(1)

client.loop_forever()
