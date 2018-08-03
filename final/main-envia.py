import random
import time
from ubidots import post_request

TOKEN = "BBFF-m1tW3P8lTsfrogcltXCkXY0dDDfb9b"  # Put your TOKEN here
DEVICE_LABEL = "teste"  # Put your device label here 

i = 30

while i != 0:
	# Criando o JSON que será enviado
	payload = {"twitter": 2018,
			   "tweets": random.randint(0,100),
			   "emergencia": random.randint(0,1)}

	print("[INFO] Attemping to send data")
	post_request(payload, DEVICE_LABEL, TOKEN) # Enviando o JSON para o ubidots
	print("[INFO] finished")

	time.sleep(5)
	i -= 1