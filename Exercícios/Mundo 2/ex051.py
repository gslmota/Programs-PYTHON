# Menu de Interações
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 0
while op != 5:
    print('Menu')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair  
    ''')
    op = int(input('Digite um valor: '))
    if op == 1:
        soma = n1 + n2
        print(' Soma {}'.format(soma))
    elif op == 2:
        mult = n1 * n2
        print('Multiplicação: {}'.format(mult))
    elif op == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        op = 0
print('Fim!')