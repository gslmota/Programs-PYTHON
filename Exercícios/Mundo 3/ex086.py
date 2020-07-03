# Aprimoramento de cadastro de jogador
time = list()
jogador = dict()
partidas = list()
while True: 
    jogador['nome'] = str(input('Digite o nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0,tot):
        partidas.append(int(input(f'Quantod gols na partida {c+1} ?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)