# Jogo de 4 pessoas usando o dado!
from random import randint
from time import sleep
from operator import itemgetter

jogadas = {}
jogadas['jogador 1'] = randint(1,6)
jogadas['jogador 2'] = randint(1,6)
jogadas['jogador 3'] = randint(1,6)
jogadas['jogador 4'] = randint(1,6)
ranking = list()
for k, v in jogadas.items():
    sleep(1)
    print(f'O {k} jogou {v}!')
ranking = sorted(jogadas.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pomtos!')
    sleep(1)
