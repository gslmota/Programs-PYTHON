# Função que realiza contagem
def contador(i, f, p):
    if i > f:
        for x in range(i, f, p):
            print(x)
    else:
        for x in range(i, f, -p):
            print(x)

# programa principal
