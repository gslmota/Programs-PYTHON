# Adicionando valores em lista e criando outras listas
valores = []
c = 0
while True:
    number = int(input('Digite um número: '))
    valores.append(number)
    c += 1
    d = (str(input('Deseja Continuar? [s/n]'))).strip().upper()
    if d == 'N':
        break