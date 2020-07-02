# Gerenciamento de jogador de futebol
jogador = {
    'Nome' : str(input('Nome: ')), 
    'Partidas' : int(input('Quantidade de partidas: '))
}
tgols = []
c = 0
qgols = 0
while c < jogador['Partidas']:
    n = int(input(f'Qual o total de gols na partida {c+1}?'))
    tgols.append(n)
    qgols += n
jogador['Gols'] = tgols[:]
jogador['Total de Gols'] = qgols
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}!')


