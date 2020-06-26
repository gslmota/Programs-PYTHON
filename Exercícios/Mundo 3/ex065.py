# Lendo valores e guardando em tupla
tup = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'O 9 apareceu {tup.count(9)} vezes.')
if 3 in tup:
    print(f'O 3 foi digitado na posição {tup.index(3)}')
else:
    print('Não existe 3 na tupla')
print('Numeros pares digitados: ')
for n in tup:
    if n % 2 == 0:
        print(n)

