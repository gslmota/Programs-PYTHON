# Ordenar lista de 5 números sem usar sort()
val = []
cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    if cont == 0 or n > val[-1]:
        val.append(n)
    else:
        pos = 0
        while pos < len(val):
            if n <= val[pos]:
                
    cont += 1
print(val)