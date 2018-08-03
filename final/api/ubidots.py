
import time
import requests

def post_request(payload, device_label, token):

    # Criando o cabeçalho da requisição HTTP
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, device_label)
    headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

    # Fazendo a requisição HTTP
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processando o resultado
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return

    print("[INFO] request made properly, your device is updated")