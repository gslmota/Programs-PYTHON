# Sorteando e guardando em tupla
from random import randint
menor = 11
maior = 0
tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
for c in range(0,5):
    if tupla[c] < menor:
        menor = tupla[c]
    elif tupla[c] > maior:
        maior = tupla[c]
print(tupla)
print(f'O maior é {maior}')
print(f'O menor é {menor}')
# ou maior = max(tuplas) menor = min(tuplas)