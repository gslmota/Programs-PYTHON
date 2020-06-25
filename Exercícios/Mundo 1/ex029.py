# existencia de triangulo
l1 = float(input('Digite o tamanho do lado 1: '))
l2 = float(input('Digite o tamanho do lado 2: '))
l3 = float(input('Digite o tamanho do lado 3: '))
if l1 < l2 + l3 or l2 < l1 + l3 or l3 < l1 + l2:
    print('Pode formar um triângulo!')
    print('Pode ser triangulos')
else:
    print('Não pode formar triângulo!')