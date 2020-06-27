# exercicio de lista 
lista = []
menor = 0
maior = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(lista)
print(f'O maior é {maior} e o menor é {menor}')
for x, z in enumerate(lista):
    if z == maior:
        print(f'O maior apareceu na posição {x}', end = '')

for x, z in enumerate(lista):
    if z == menor:
        print(f'O menor apareceu na posição {x} ', end = '')
print('FIM!')