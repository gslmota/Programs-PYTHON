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
print(f'{"No.":< 4}{"Nome":< 10}')
for i, a in enumerate(ficha):
    print(f'{i:< 4}{a[0]:< 10}{a[2]:> 8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? 0 para'))
    if opc == 0:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')