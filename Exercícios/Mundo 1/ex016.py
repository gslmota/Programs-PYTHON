# nome da pessoa e informações
nome = str(input('Digite o nome: ')).strip() # serve para eliminar os espaços 
print( 'Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# poderia ser assim
# separa = nome.split()
# separa[0] seria o primeiro nome e len(separa[0]) a quantidade de letras