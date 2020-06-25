# número maior
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2 :
    maior = n1
elif n1 == n2 :
    maior = " Nenhum, pois são iguais!2"
else :
    maior = n2
print('O maior é {}'.format(maior))