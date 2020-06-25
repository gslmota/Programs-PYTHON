# Números ímpares múltiplos de 3
s = 0
for n in range(1,500):
    if n % 2 != 0:
        if n % 3 == 0:
            s += n
print('A soma dos valores é: {}'.format(s))
      