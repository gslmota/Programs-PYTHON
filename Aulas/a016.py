# Aula de Modularização
def fatorial(numero):
    f = 1
    for c in range(1, numero + 1):
        
# Programa principal
num =  int(input("Digite um numero: "))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}!')