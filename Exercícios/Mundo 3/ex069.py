# Adicionar varios valores em um lista
lista = [] # ou lista = val()
while True:
    n = (int(input('Digite um número: ')))
    if n in lista:
        print('Este valor não pode ser adiconado pois já existe!')
    else:
        lista.append(n)
        print('Valor lido com sucesso!')
    d = (str(input('Deseja Continuar? [s/n]'))).strip().upper()
    if d == 'N':
        break
lista.sort()
print(lista)