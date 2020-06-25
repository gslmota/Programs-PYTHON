# Cadastro de Pessoas
tp = th = tm = 0
while True:
    idade = int(input('Digite a sua idade:'))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o seu sexo: ')).strip().upper()[0]
    if idade >= 18:
        tp += 1
    if sexo == 'M':
        th += 1
    if sexo == 'F' and idade < 20:
        tm += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Acabou!!!')
print(f'Total de pessoas com mais de 18 anos: {tp}')
print(f'Total de homes cadastrados {th}')
print(f'Total de mulheres com menos de 20 anos {tm}')


