# Boletim com listas Compostas
ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], med])
    n = str(input ('Deseja Continuar? S/N')).strip()
    if n in 'Nn':
        break
print(ficha)
print(f'{None:<4}{None}')