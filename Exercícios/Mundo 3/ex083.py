# Cadastro de trabalhador 
from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['nascimento'] = int(input('Data de Nascimento: '))
print(cadastro['nascimento'])
data = cadastro['nascimento']
ano = date.year
idade = ano - data
cadastro['idade'] = idade
if cadastro['idade'] >= 35:
    cadastro['aposentadoria'] = 'Você pode se aposentar!'
else:
    cadastro['aposentaria'] =  'Você não pose se aposentar!'
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')