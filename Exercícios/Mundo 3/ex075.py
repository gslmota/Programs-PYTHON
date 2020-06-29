# Listas Compostas
dado = list()
galera = list()
quant = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input ('Peso: ')))
    galera.append(dado[:])
    dado.clear()
    quant += 1
    n = str(input ('Deseja Continuar? S/N')).strip()
    if n in 'Nn':
        break
    for p in galera:
        if p[1] > 100:
            print(f'{p[0]} é de  maior peso!')
        elif p[1] < 70:
            print(f'{p[0]} é de menor peso!')