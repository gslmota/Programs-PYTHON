# Aprimoramento de cadastro de jogador
time = list()
jogador = dict()
partidas = list()
while True: 
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantod gols na partida {c+1} ?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    r = str(input('Quer continuar ?[S/N]'))
    if r in 'Nn':
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4}', end ='')
    for d in k.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-' * 40)