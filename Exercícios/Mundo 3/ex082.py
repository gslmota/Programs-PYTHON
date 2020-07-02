# Jogo de 4 pessoas usando o dado!
from random import randint
from time import sleep
jogadas = {}
jogadas['jogador 1'] = randint(1,6)
jogadas['jogador 2'] = randint(1,6)
jogadas['jogador 3'] = randint(1,6)
jogadas['jogador 4'] = randint(1,6)
for k, v in jogadas.items():
    sleep(1)
    print(f'O {k} jogou {v}!')
