# verifica frase
frase = str(input('Digite um frase: ')).lower().strip()
print(' A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+ 1))
print('A últoma letra apareceu na posição {}'.format(frase.rfind('a')+ 1))