# Fazendo operações em uma matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l} {c}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end = '')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('A soma dos valores pares é {}'.format(spar))
for l in range(0, 3):
    scol += matriz[l][2]
print('A soma dos valores da 3 coluna é {}'.format(scol))
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    else:
        if matriz[1][c] > mai:
            mai = matriz[1][c]
print('O maior valor é {}'.format(mai))