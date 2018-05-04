from libsoc_zero.GPIO import Button
from time import sleep

segundos = 10

btn1 = Button('GPIO-A')
btn2 = Button('GPIO-C')

path = 'dados.txt'
arquivo = open(path, 'w')

while segundos != 0:
    sleep(1)
    if btn1.is_pressed():
        arquivo.write('O touch foi pressionado!\t')
    else:
        arquivo.write('O touch não foi pressionado!\t')

    if btn2.is_pressed():
        arquivo.write('Há luz no ambiente!\n')
    else:
        arquivo.write('Não há luz no ambiente!\n')

    segundos -= 1

arquivo.close()
