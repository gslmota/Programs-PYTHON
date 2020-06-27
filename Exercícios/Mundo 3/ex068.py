# exercicio de lista 
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
print(lista)
menor = min(lista)
maior = max(lista)
print(f'O maior é {maior} e o menor é {menor}')