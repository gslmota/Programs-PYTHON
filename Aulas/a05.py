#arquivos coloridos no terminal
print('\033[31;43mHello world!\033[m')

nome = 'Gabriel'
print('Seu nome é: {}{}{}'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa' : '\033[m', 'azul' : '\033[34m', 'vermelho' : '\033[31m'}
idade = 20
print('Sua idade é: {}{}{}'.format(cores['vermelho'],idade, cores['limpa']))