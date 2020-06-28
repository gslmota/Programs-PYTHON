# Adicionando valores em lista e criando outras listas
valores = []
pares = []
impares = []
while True:
    number = int(input('Digite um número: '))
    valores.append(number)
    d = (str(input('Deseja Continuar? [s/n]'))).strip().upper()
    if d == 'N':
        break