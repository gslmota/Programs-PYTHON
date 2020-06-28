# Exercicio 072 de outra forma
valores = []
pares = []
impares = []
while True:
    number = int(input('Digite um número: '))
    valores.append(number)
    d = (str(input('Deseja Continuar? [s/n]'))).strip().upper()
    if d == 'N':
        break
for p, n in enumerate(valores):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)