# Cadastro de trabalhador 
from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['nascimento'] = int(input('Data de Nascimento: '))
idade = date.year - cadastro['nascimento']
cadastro['idade'] = idade
if cadastro['idade'] >= 35:
    cadastro['aposentadoria'] = 'Você pode se aposentar!'