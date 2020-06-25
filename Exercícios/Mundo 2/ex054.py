# Super PA 3.0
ptermo = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
qtermos = int(input('Digite a quantidade de termos: '))
c = qtermos
while c != 0: 
        print('{}'.format(ptermo))
        ptermo += raz
        c -= 1
        if c == 0:
            nter = int(input('Você deseja mostrar mais termos? Digite a quantidade desejada: '))
            c = nter
