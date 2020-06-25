# Jogo jokenpô
cores = {'limpa' : '\033[m', 'azul' : '\033[34m', 'vermelho' : '\033[31m', 'amarelo': '\033[33m', 'verde' : '\033[32m'}
from random import randint
print('===Jokenpô=======')
print('Escolha uma opção:')
print(' 0-> Pedra')
print(' 1-> Papel')
print(' 2-> Tesoura')
escolhas = ('Pedra', 'Papel', 'Tesoura')
jogada = int(input('Qual é a sua jogada ?'))
print('-' * 18)
print('''Jo
Ken
Pô!''')
print('-' * 18)
jogadapc = randint(0,2)
if jogada == 0 and jogadapc == 0 or jogada == 1 and jogadapc == 1 or jogada == 2 and jogadapc == 2:
    print('Computador Jogou {}{}{}'.format(cores['amarelo'], escolhas[jogadapc], cores['limpa']))
    print('-' * 25)
    print('Jogador Jogou {}{}{}'.format(cores['amarelo'], escolhas[jogada], cores['limpa']))
    print('-' * 25)
    print('{}EMPATOU!{}'.format(cores['verde'],  cores['limpa']))
elif jogada == 0 and jogadapc == 2 or jogada == 2 and jogadapc == 1 or jogada == 1 and jogadapc == 0:
    print('Computador Jogou {}{}{}'.format(cores['amarelo'], escolhas[jogadapc], cores['limpa']))
    print('-' * 25)
    print('Jogador Jogou {}{}{}'.format(cores['amarelo'], escolhas[jogada], cores['limpa']))
    print('-' * 25)
    print('{}Jogador VENCEU!{}'.format(cores['azul'],  cores['limpa']))
elif  jogada == 0 and jogadapc == 1 or jogada == 1 and jogadapc == 2 or jogada == 2 and jogadapc == 0:
    print('Computador Jogou {}{}{}'.format(cores['amarelo'], escolhas[jogadapc], cores['limpa']))
    print('-' * 25)
    print('Jogador Jogou {}{}{}'.format(cores['amarelo'], escolhas[jogada], cores['limpa']))
    print('-' * 25)
    print('{}Computador VENCEU!{}'.format(cores['vermelho'],  cores['limpa']))