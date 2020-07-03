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
print('cod', end = '')
for i in jogador.keys():
    print(f'{i:<15}', end = '')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end ='')
    for d in k.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-' * 40)
while True:
    bus = int(input('Digite o número do jogador que você deseja buscar os dados: [00 para a busca]'))
    if bus == 00:
        break
    print(f'Levantamento de Jogador {time[bus] ["nome"]}: ')
    for i, g in enumerate(time[bus]['gols']):
        print(f'    No jogo {i + 1} fez {g} gols!')
    print('-' * 40)
print('Fim!')