# Aula de listas parte 2
teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
print(galera)


galera = [['joao', 23], ['maria', 43], ['pedro', 23]]
print(galera)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade!')


dado = list()
galera = list()
tmaior = tmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input ('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade!')
        tmaior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        tmenor += 1
print(f'Temos {tmaior} de idade e {tmenor} de idade!')