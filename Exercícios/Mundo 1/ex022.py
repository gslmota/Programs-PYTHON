# Joguinho do número!
import random
npc = random.randint(1,5)
nuser = int(input('Digite um número: '))
if nuser == npc:
    print('O usuário veceu!')
else:
    print('O computador venceu!')