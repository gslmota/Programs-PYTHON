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
