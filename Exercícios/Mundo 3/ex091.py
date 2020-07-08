# Sortear números e somar
from random import randint
from time import sleep
def sortearLista(lista):
    print('Sorteando 5 valores para a lista: ', end ='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end = '', flush = True)
        sleep(0.3)
    print(' Pronto!!!')

def somaPares(lista):
    soma = 0
    for val in lista:
        if val % 2 == 0:
            soma += val
    print(f'Somando os valores pares de {lista}, temos {soma}')   

# Programa principal
num = list()
sortearLista(num)
somaPares(num)