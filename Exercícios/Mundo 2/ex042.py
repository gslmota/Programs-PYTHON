# Número primo
numero = int(input('Digite o número: '))
qdiv = 0
for n in range(1, numero + 1):
    if numero % n == 0:
        qdiv += 1
if qdiv == 2:
    print('Número Primo!!!')