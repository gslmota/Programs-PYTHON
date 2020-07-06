# Aula de Funções

valores =[2, 3, 5, 6, 89]
def linha():
    print('-' * 30)


def mensagem(msg):
    linha()
    print(msg)
    linha()



def dobra(lst):
    cont = 0
    while cont < len(lst):
        lst[cont] *= 2
    cont += 1

def soma(a,b):
    s = a + b
    print(s)


def contador(*n):
    for v in n:
        print(v)
# Programa principal
linha()
print('Olá mundo!')
linha()
mensagem('Oi tudo bem?')
soma(2,54)

contador(1, 3)
contador(1, 3, 4, 5, 6)
contador(3)
dobra(valores)