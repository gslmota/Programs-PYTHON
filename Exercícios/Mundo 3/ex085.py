# Unindo dicionarios e listas
pessoas = {}
dadosPessoas = []
tcadastrada = 0
soma = media = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Digite o seu nome: ')).strip()
    pessoas['Sexo'] = str(input('Digite o seu sexo: [M/F]')).strip().upper()
    pessoas['Idade'] = int(input('Digite a sua idade: '))
    soma += pessoas['Idade']
    dadosPessoas.append(pessoas.copy())
    tcadastrada += 1
    s = str(input('Deseja Continuar? [S/N]'))
    if s in 'Nn':
        break
print(f'Foram cadastradas {tcadastrada} pessoas!')
media = soma / len(dadosPessoas)
print(f'A media de idade é {media} anos!')
print('As mulheres cadastradas foram: ', end = '')
for p in dadosPessoas:
    if p['Sexo'] == 'F':
        print(f'{p[" Nome"]}', end = '')
print()
print('Pessoas acima da media de idade: ', end = '')
for c in dadosPessoas:
    if c['Idade'] > media:
        print(f'{c["Nome"]}', end = '')
        print()
print('FIM!')