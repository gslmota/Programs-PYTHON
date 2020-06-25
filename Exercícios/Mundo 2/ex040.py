# Soma dos valores pares de 6 inteiros
s = 0
for n in range(0,6):
    x = int(input ('Digite um número: '))
    if x % 2 == 0:
        s += x
print('A soma dos valores é: {}'.format(s))
      
    