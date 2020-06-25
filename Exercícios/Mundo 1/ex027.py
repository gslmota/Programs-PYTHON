# maior e menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite novamente mais um número: '))
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n3:
        maior = n2
    else:
        maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n3:
    menor = n2
else:
    menor = n3

print('O maior é {}'.format(maior))
print('O menor é {}'.format(menor))