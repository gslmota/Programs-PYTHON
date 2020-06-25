# Busca String 
nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer {}!'.format(nome))
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n) - 1]))

