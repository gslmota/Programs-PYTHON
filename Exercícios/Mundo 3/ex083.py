# Cadastro de trabalhador 
from datetime import datetime
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['nascimento'] = int(input('Data de Nascimento: '))
print(cadastro['nascimento'])
data = cadastro['nascimento']
ano = datetime.now().year
idade = ano - data
cadastro['idade'] = idade
if cadastro['idade'] >= 35:
    cadastro['aposentadoria'] = 'Você pode se aposentar!'
else:
    cadastro['aposentaria'] =  'Você não pode se aposentar!'
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')