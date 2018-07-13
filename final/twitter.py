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
GEOCODE = '-23.533773,-46.625290,30km' # Localização 'latitude,longitude,raio/km'

class Twitter:
    def __init__(self, query):
        self.query = query
        self.primeira_busca = True
        self.twitter_id = None

    def filtra_resultado_sem_id(self, search_results):
        i = 0

        for tweet in search_results['statuses']:

            dados = {} # Cria o objeto JSON
            dados['username'] = tweet['user']['screen_name'].encode('utf-8') # Adicionando no JSON o username
            dados['created_at'] = tweet['created_at'].encode('utf-8') # Adicionando o momento que o tweet foi criado

            if i == 0:
                hora = int(dados['created_at'].split()[3].split(':')[0])
                minuto = int(dados['created_at'].split()[3].split(':')[1])
                segundo = int(dados['created_at'].split()[3].split(':')[2])
                primeiro = datetime.time(hora, minuto, segundo)
                self.twitter_id = tweet['id']

            # print "Tweet from @%s Date: %s" % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'].encode('utf-8'))

            if tweet['place'] == None:
                dados['location'] = 'not defined' # Caso não definida a localização, coloca not defined
                # print "Location: not defined!"
            else:
                dados['location'] = tweet['place']['full_name'] # Adicionando a localização no JSON
                # print "Location: %s" % (tweet['place']['full_name'])

            dados['text'] = tweet['text'].encode('utf-8') # Adicionando o conteudo ao JSON

            # print "Text: %s" % (tweet['text'].encode('utf-8')),"\n"

            # tweets.append(dados)
            i += 1

            if i > 6:
                break

            # print json.dumps(dados, indent=4) # Imprime o JSON com identação 4
            hora = int(dados['created_at'].split()[3].split(':')[0])
            minuto = int(dados['created_at'].split()[3].split(':')[1])
            segundo = int(dados['created_at'].split()[3].split(':')[2])
            ultimo = datetime.time(hora, minuto, segundo)


        print "primeiro = %s" % primeiro
        print "ultimo = %s" % ultimo

        duration = datetime.datetime.combine(datetime.date.min, primeiro) - datetime.datetime.combine(datetime.date.min, ultimo)
            # diferenca = ultimo - primeiro


            # print duration < datetime.timedelta(0, 30)

            # print "diferença =", duration
            # print "datetime.timedelta(0, 0, 30) =", datetime.timedelta(0, 30)
            # print "menor que 30 =",

        if i < 6:
            print 'nao faz nada'
        else:
            if duration < datetime.timedelta(0, 30):
                print '6 tweets em 30 segundos'
            else:
                print 'palavra de emergencia?'


    def filtra_resultado_com_id(self, search_results):
        tweets, i = [], 0

        print 'verificando tweets desde o último'
        for tweet in search_results['statuses']:

            if i == 0:
                self.twitter_id = tweet['id']
                i += 1

            dados = {} # Cria o objeto JSON
            dados['username'] = tweet['user']['screen_name'].encode('utf-8') # Adicionando no JSON o username
            dados['created_at'] = tweet['created_at'].encode('utf-8') # Adicionando o momento que o tweet foi criado

            print "Tweet from @%s Date: %s" % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'].encode('utf-8'))

            if tweet['place'] == None:
                dados['location'] = 'not defined' # Caso não definida a localização, coloca not defined
                # print "Location: not defined!"
            else:
                dados['location'] = tweet['place']['full_name'] # Adicionando a localização no JSON
                # print "Location: %s" % (tweet['place']['full_name'])

            dados['text'] = tweet['text'].encode('utf-8') # Adicionando o conteudo ao JSON

            # print "Text: %s" % (tweet['text'].encode('utf-8')),"\n"

            tweets.append(dados)

            #  print json.dumps(dados, indent=4) # Imprime o JSON com identação 4

        print 'saiu!'
        return len(tweets)

    def busca(self):
        # Criando uma nova instância do twitter com autenticação de leitura oAuth = 2
        twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

        # Recuperando o Token de Acesso
        ACCESS_TOKEN = twitter.obtain_access_token()

        # Recriando a instância com o token de acesso
        twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

        # Buscando pela Hashtag
        #search_results = twitter.search(q="#Neymar", rpp="10", geocode=GEOCODE)
        if self.primeira_busca:
            search_results = twitter.search(q=self.query)
            self.filtra_resultado_sem_id(search_results)
            self.primeira_busca = False
        else:
            search_results = twitter.search(q=self.query, since_id=self.twitter_id)
            qtdd = self.filtra_resultado_com_id(search_results)

            if qtdd > 6:
                return "enviar mensagem"
            else:
                return "nao envia"

        #print search_results['statuses'][0]
