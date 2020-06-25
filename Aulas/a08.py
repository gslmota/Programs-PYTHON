# repetição com o While
c = 1
while c < 10:
    print('Oi')
    c += 1
# Deve se usar o while quando não sabe a condição de parada!

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você Digitou {} números pares e {} números ímpares!'.format(par, impar))