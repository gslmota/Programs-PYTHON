# Aula de Dicionários
dados = dict()
dados = {'nome': 'Pedro','idade': 23}
print(dados['nome'])
print(dados['idade'])
print(f'O {dados["nome"]} tem {dados["idade"]} anos de idade!')
print(dados.keys())
print(dados.values())
print(dados.items())

for k in dados.keys():
    print(k) 

del dados['nome']



# Criando um dicionario dentro de uma lista
brasil = []
estado1 = {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'}
estado2 = {'uf' : 'Minas Gerais', 'sigla' : 'MG'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)