# Contiuação da aula de funções

# interactive help
 # Função help que ajuda em qualquer coisa -> help () ou help(nome do comando ex : print)
 # help(input) é a mesma coisa que print(input.__doc__)

 # docstrings
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i -> inicio da contagem
    :param f -> final da contagem
    :param p -> passo da contagem
    :return -> sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end = '')
        c += p
    print('Fim!')


# Programa principal
contador(2, 20, 5)
help(contador)

# Parametros Opcionais
# Esse parametros servem para complementar valores faltantes

def somar(a = 0, b = 0, c = 0):
    s = a + b + c
    print(s)

# programa principal
somar(2, 3)
# e possivel nomear os parametros fazendo assim -> somar(c = 9, b = 3)

# Escopo de variaveis
# variaveis em funções sao locais
# fora elas sao globais / para fazer as modificações deve se colocar global namevariavel
