# Interronpendo while
cont = 1
while cont <= 1:
    print(cont)
    cont += 1
print('FIM!')


soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    soma += n
print('Deu tudo certo!')
print(f'A soma é {soma}')