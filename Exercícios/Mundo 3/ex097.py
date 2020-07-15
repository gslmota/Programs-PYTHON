# Sistema de ajuda em Python
def ajuda(com):
    help(com)


def título(msg, cor):
    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)
#Programa Principal
comando = ''
while True:
    print('Sistema de Ajuda!')
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)