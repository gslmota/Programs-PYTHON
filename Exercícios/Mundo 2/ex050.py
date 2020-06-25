# Joguinho do número 2.0
import random
cont = 0
npc = random.randint(1,10)
nuser = -1
while nuser != npc:
    nuser = int(input('Digite um número: '))
    cont += 1
    if nuser != npc:
         print('O computador venceu!')
if nuser == npc:
    print('O usuário veceu!')
    print('O usuário jogou {} vezes.'.format(cont))