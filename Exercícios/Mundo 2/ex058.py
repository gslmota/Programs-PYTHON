# Tabuada de vários números 3.0
while True:
    n = int(input('Digite o valor que deseja ver a tabuada: '))
    if n < 0:
        break
    else:
        print('-' * 30)
        for c in range(1,11):
            print(f'{n} x {c} = {n * c}')
        print('-' * 30)
