# -*- coding: utf-8 -*-

from twitter import Twitter
import time

'''
    Inicializando o o objeto Twitter
    Parametros:
        1 - texto que sera procurado pela API
        2 - Palavra de emergencia, caso encontrada devera enviar uma mensagem
        3 - Tempo de diferença entre os tweets para enviar a mensagem em SEGUNDOS
        4 - Quantidade de tweets necessários para enviar a mensagem
'''
t = Twitter('#neymar', 'se jogou', 30, 6)

i = 5

while i != 0:

    '''
        O método busca, volta se devemos enviar a mensagem ou não
        True = devemos enviar a mensagem
        False = não devemos enviar
    '''
    if t.busca():
        print 'Enviar mensagem'
    else:
        print 'Tudo sob controle :)'

    time.sleep(5)
    i -= 1
