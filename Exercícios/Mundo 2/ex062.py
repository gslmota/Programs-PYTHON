# Simulador de Caixa Eletrônico
print('=' * 30)
print('{:^30}'.format('BANCO'))
print('=' * 30)
valor = int(input('Digite o valor que deseja sacar: '))
total = valor
ced = 50
tced = 0 
while True:
    if total >= ced:
        total -= ced
        tced += 1
    else:
        if tced > 0:  
            print(f'Total de {tced} cédulas de {ced} reais!')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            tced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre!')
