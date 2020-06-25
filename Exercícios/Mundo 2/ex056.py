# Soma n números diferentes
x = int(input('Digite um número: '))
soma = qn = 0
while x != 999:
    soma = soma + x
    qn += 1
    x = int(input('Digite outro número: '))
print(' O valor da soma de {} números digitados foi: {}'.format(qn , soma))