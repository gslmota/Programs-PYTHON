# Aula de Funções
def linha():
    print('-' * 30)


def mensagem(msg):
    linha()
    print(msg)
    linha()



def soma(a,b):
    s = a + b
    print(s)


def contador(*n):
    print(n)
# Programa principal
linha()
print('Olá mundo!')
linha()
mensagem('Oi tudo bem?')
soma(2,54)

contador(1, 3)
contador(1, 3, 4, 5, 6)
contador(3)