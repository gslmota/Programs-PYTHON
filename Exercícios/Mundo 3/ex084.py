# Gerenciamento de jogador de futebol
jogador = {
    'Nome' : str(input('Nome: '))
}
z = int(input('Quantidade de partidas: '))
tgols = []
c = 0
qgols = 0
while c < z:
    n = int(input(f'Qual o total de gols na partida {c+1}?'))
    tgols.append(n)
    qgols += n
    c += 1
jogador['Gols'] = tgols[:]
jogador['Total de Gols'] = qgols
print(jogador)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}!')

print(f'O jogador {jogador["Nome"]} jogou {z} partidas!')
tp = z
x = 0
while x < tp:
    print(f'Na partida{x+1}, fez {tgols[x]}')
print(f'O jogador {jogador["Nome"]} fez {qgols} gols!')
