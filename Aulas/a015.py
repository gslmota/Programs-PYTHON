# Contiuação da aula de funções

# interactive help
 # Função help que ajuda em qualquer coisa -> help () ou help(nome do comando ex : print)
 # help(input) é a mesma coisa que print(input.__doc__)

 # docstrings
def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c}', end = '')
        c += p
    print('Fim!')


# Programa principal
contador(2, 20, 5)