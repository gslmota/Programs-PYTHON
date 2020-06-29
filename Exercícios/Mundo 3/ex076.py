# Lista para Cadastrar Números
lis = [[], []]
val = 0
for c in range(1,8):
    val = int(input('Digite um número: '))
    if val % 2 == 0:
        lis[0].append(val)
    else:
        lis[1].append(val)
lis[0].sort()
lis[1].sort()
print(lis[0])
print(lis[1])