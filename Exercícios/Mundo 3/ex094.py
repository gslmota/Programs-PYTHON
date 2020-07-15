# Ficha de jogador
def ficha(nome = '<desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} no campeonato!')


# Programa principal
nome = str(input('Nome: '))
gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else: 
    gols = 0

if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome, gols)