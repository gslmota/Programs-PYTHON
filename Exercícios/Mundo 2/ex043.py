# Verifica Palíndromo
frase = str(input('Digite uma frase ou palavra:  ')).strip().upper()
wor = frase.split()
tjun = ''.join(wor)
inverso = ''
for c in range(len(tjun) - 1, -1, -1):
    inverso += tjun[c]
if inverso == tjun:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')