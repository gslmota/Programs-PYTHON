# Soma dos valores de uma PA 2.0 
ptermo = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
print('Os 10 primeiros termos: ')
c = 10
while c >= 1: 
        print('{}'.format(ptermo))
        ptermo += raz
        c -= 1