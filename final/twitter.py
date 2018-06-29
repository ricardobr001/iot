# -*- coding: utf-8 -*-
from twython import Twython
APP_KEY = 'BGduVvapnt8S51jwdLePhHDyW'
APP_SECRET = 'WiRWnfryuUzyxmsVjRrvdNIkXbZ7ahDl4OOrsq4QycAl8FSDRc'
GEOCODE = '-23.533773,-46.625290,30km' # Localização 'latitude,longitude,raio/km'

# Criando uma nova instância do twitter com autenticação de leitura oAuth = 2
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)

# Recuperando o Token de Acesso
ACCESS_TOKEN = twitter.obtain_access_token()

# Recriando a instância com o token de acesso
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

# Buscando pela Hashtag
#search_results = twitter.search(q="#Neymar", rpp="10", geocode=GEOCODE)
search_results = twitter.search(q="#testeiot2018aulabccs", rpp="10")

#print search_results['statuses'][0]

for tweet in search_results['statuses']:
    print "Tweet from @%s Date: %s" % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at'].encode('utf-8'))
    
    if tweet['place'] == None:
        print "Location: not defined!"
    else:
        print "Location: %s" % (tweet['place']['full_name'])

    print "Text: %s" % (tweet['text'].encode('utf-8')),"\n"
