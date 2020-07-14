# Função que calcula fatorial
def fatorial(num, show = False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


