# -*- coding: utf-8 -*-

'''
    link util: https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
    https://twython.readthedocs.io/en/latest/api.html#twython.Twython.search
'''
from twython import Twython
import json
import datetime

APP_KEY = 'BGduVvapnt8S51jwdLePhHDyW'
APP_SECRET = 'WiRWnfryuUzyxmsVjRrvdNIkXbZ7ahDl4OOrsq4QycAl8FSDRc'
#GEOCODE = '-23.533773,-46.625290,30km' # Localização 'latitude,longitude,raio/km'

class Twitter:
    def __init__(self, query, emergencia, tempo, qtdd_tweets):
        self.query = query
        self.primeira_busca = True
        self.twitter_id = None
        self.emergencia = emergencia
        self.tempo = tempo
        self.qtdd_tweets = qtdd_tweets

    def filtra_resultado_sem_id(self, search_results):
        i = 0 # Inicializando a variavel

        for tweet in search_results['statuses']:

            dados = {} # Cria o objeto JSON
            dados['created_at'] = tweet['created_at'].encode('utf-8') # Adicionando o momento que o tweet foi criado

            # Salvando a hora, minuto e segundo do primeiro tweet encontrado e seu id
            if i == 0:
                hora = int(dados['created_at'].split()[3].split(':')[0])
                minuto = int(dados['created_at'].split()[3].split(':')[1])
                segundo = int(dados['created_at'].split()[3].split(':')[2])
                primeiro = datetime.time(hora, minuto, segundo)
                self.twitter_id = tweet['id']

            # Se encontrar a palavra de emergencia no tweet, retorna que deve enviar a mensagem
            if self.emergencia in tweet['text'].encode('utf-8'):
                return True

            i += 1
            if i > self.qtdd_tweets:
                break

            # Salvando a hora, minuto e segundo do ultimo tweet encontrado
            hora = int(dados['created_at'].split()[3].split(':')[0])
            minuto = int(dados['created_at'].split()[3].split(':')[1])
            segundo = int(dados['created_at'].split()[3].split(':')[2])
            ultimo = datetime.time(hora, minuto, segundo)

        # Subtraindo a diferença de tempo entre o primeiro e ultimo tweet encontrado
        duration = datetime.datetime.combine(datetime.date.min, primeiro) - datetime.datetime.combine(datetime.date.min, ultimo)

        # Se a busca voltou menos de 6 tweets, não deve enviar uma mensagem
        if i < self.qtdd_tweets:
            return False
        else:
            # Caso contrário, verifica se a difença de tempo entre os dois tweets foi mais de 30 segundos
            if duration < datetime.timedelta(0, self.tempo):
                return True
            else:
                return False


    def filtra_resultado_com_id(self, search_results):
        tweets, i = [], 0 # Inicializando as variaveis

        for tweet in search_results['statuses']:

            # Salvando o id do primeiro tweet
            if i == 0:
                self.twitter_id = tweet['id']

            # Se encontrar a palavra de emergencia no tweet, retorna que deve enviar a mensagem
            if self.emergencia in tweet['text'].encode('utf-8'):
                return self.qtdd_tweets + 1

            i += 1

        return i

    def busca(self):
        # Criando uma nova instância do twitter com autenticação de leitura oAuth = 2
        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

        # Recuperando o Token de Acesso
        ACCESS_TOKEN = twitter.obtain_access_token()

        # Recriando a instância com o token de acesso
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

        # Se for a primeira busca
        if self.primeira_busca:
            search_results = twitter.search(q=self.query) # Buscamos pela hashtag passada no main
            res = self.filtra_resultado_sem_id(search_results) # Filtramos os resultados obtivos
            self.primeira_busca = False # Setamos que não será mais feito a primeira busca

            # Se a quantidade de tweets for igual a 6, devemos enviar uma mensagem
            return res
        # Caso contrário
        else:
            search_results = twitter.search(q=self.query, since_id=self.twitter_id)
            qtdd = self.filtra_resultado_com_id(search_results)

            # Se a quantidade de tweets for superior a 6, envia a mensagem
            if qtdd > self.qtdd_tweets:
                return True
            else:
                return False