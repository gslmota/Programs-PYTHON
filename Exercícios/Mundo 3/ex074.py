# Verifica parênteses
lista = []
exp = str(input('Digite a expressão: '))
lista.append(exp)
print(lista)
cont = 0
for p, n in enumerate(lista):
    if lista[p] == '(' or lista[p] == ')':
        cont += 1
if cont % 2 == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')