# Sortear números e somar
from random import randint
from time import sleep
def sortearLista(lista):
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end = '', flush = True)
        sleep(0.3)
    print('Pronto!!!')

def somaPares():



# Programa principal
num = list()
sortearLista(num)