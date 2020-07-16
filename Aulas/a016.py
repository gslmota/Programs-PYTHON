# Aula de Modularização
def fatorial(numero):
    f = 1
    for c in range(1, numero + 1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3
# Programa principal
num =  int(input("Digite um numero: "))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}!')
print(f'O dobro de {num} é {dobro(num)}!')
print(f'O triplo de {num} é {triplo(num)}!')