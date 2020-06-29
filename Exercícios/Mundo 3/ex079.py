# Criando Sorteio MEGA SENA
from random import randint
from time import sleep
lis = list()
jogos = list()
tjog = int(input('Deseja fazer quantos jogos?'))
q = 1
while q <= tjog:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lis:
            lis.append(num)
            cont += 1
        if cont >= 6:
            break
    lis.sort()
    jogos.append(lis[:])
    lis.clear()
    q += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)

