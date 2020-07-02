# Unindo dicionarios e listas
pessoas = {}
dadosPessoas = []
tcadastrada = 0
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Digite o seu nome: ')).strip()
    pessoas['Sexo'] = str(input('Digite o seu sexo: [M/F]')).strip().upper()
    pessoas['Idade'] = int(input('Digite a sua idade: '))
    dadosPessoas.append(pessoas.copy())
    tcadastrada += 1
    s = str(input('Deseja Continuar? [S/N]'))
    if s in 'Nn':
        break
print(f'Foram cadastradas {tcadastrada} pessoas!')
