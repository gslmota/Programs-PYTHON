# Media de n números diferentes
# condição de parada é 999
x = int(input('Digite um número: '))
soma = qn = menor = maior = c = 0
while x != 999:
    if x > maior:
        maior = x
    if x <= maior:
        if c == 0:
            menor = x
            c += 1
        else:
            if x < menor:
                menor = x
    soma = soma + x
    qn += 1
    x = int(input('Digite outro número: '))
media = soma / qn
print('O valor da soma de {} números digitados foi: {}'.format(qn , soma))
print('O valor da media foi: {}'.format(media))
print('O maior foi {} e o menor foi {}'.format(maior, menor))