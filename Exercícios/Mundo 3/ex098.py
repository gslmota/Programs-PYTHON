# funções aprofudadas em python
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número válido!')
            continue
        else:
            return n


# Programa principal
