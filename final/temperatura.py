# -*- coding: utf-8 -*-

'''
    Essa API verifica a temperatura em (http://weather.yahoo.com)
'''

from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS) # Inicializando o novo objeto
local = weather.lookup_by_location('sorocaba') # Recuperando a condição de sorocaba

condicao = local.condition # Condição gerais
clima = condicao.text # Como está o tempo atual
temperatura = condicao.temp # Temperatura atual

print 'Sorocaba - string'
print 'Clima: ' + clima.encode('utf-8')
print 'Temperatura: ' + temperatura.encode('utf-8')


# Recuperando com latitute e longitude
latlong = weather.lookup_by_latlng(-23.5062,-47.4559)

condicao = latlong.condition # Condição gerais
clima = condicao.text # Como está o tempo atual
temperatura = condicao.temp # Temperatura atual

print '\nSorocaba - latitute longitude'
print 'Clima: ' + clima.encode('utf-8')
print 'Temperatura: ' + temperatura.encode('utf-8')