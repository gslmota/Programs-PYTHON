# Verifica o peso de 5 pessoas
mp = 0
mn = 200
for n in range(0,5):
    peso = float(input ('Digite o peso: '))
    if peso > mp:
        mp = peso
    if peso < mn:
        mn = peso
print ('O maior peso é {} '.format(mp))
print('O menor peso é {} '.format(mn))