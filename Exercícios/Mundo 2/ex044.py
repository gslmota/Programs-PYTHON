# Verifica Maioridade de 7 pessoas
np = 0
for n in range(0,7):
    idade = int(input ('Digite a idade: '))
    if idade >= 21:
        np += 1
print ('Existem {} pessoas maiores de idade!'.format(np))
print('Existem {} pessoas menores de idade!'.format(7 - np))