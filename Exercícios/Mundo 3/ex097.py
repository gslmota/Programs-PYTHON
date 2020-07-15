# Sistema de ajuda em Python
from time import sleep
cores = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m')
def ajuda(com):
    título(f'Acessando o manula do comando \'{com}\'', 4)
    print(cores[6], end = '')
    help(com)
    print(cores[0], end = '')
    sleep(2)

def título(msg, cor = 0):
    tam = len(msg) + 4
    print(cores[cor], end = '')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(cores[0], end = '')
    sleep(1)

#Programa Principal
comando = ''
while True:
    título('Sistema de Ajuda!', 2)
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('Até Logo!', 1)