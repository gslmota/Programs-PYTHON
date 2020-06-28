# Colocar valores em uma lista e fazer algumas verificações
valores = []
c = 0
while True:
    number = int(input('Digite um número: '))
    valores.append(number)
    c += 1
    d = (str(input('Deseja Continuar? [s/n]'))).strip().upper()
    if d == 'N':
        break
print(f'Foram digitados {c} números')
valores.sort(reverse = True)
print(f'{valores}')
if 5 in valores:
    print(f'O 5 foi Digitado e esta na posição {valores.index(5) + 1}')