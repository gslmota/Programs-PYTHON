# Jogo do Par ou Ímpar
from random import randint
vit = 0
while True:
    jpe = int(input('Digite um número: '))
    npc = randint(1,11)
    soma = (npc + jpe)
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('Voce Jogou {} o computador jogou {} o total é {}'.format(jpe, npc, soma))
    print('Deu PAR' if soma % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Voce Venceu!')
            vit += 1
        else:
            print('Voce Perdeu!')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print('Voce Venceu!')
            vit += 1
        else:
            print('Voce Perdeu!')
            break
    print('Vamos Jogar Novamente!')
print(f'Game Over! Voce venceu {vit} vezes!')