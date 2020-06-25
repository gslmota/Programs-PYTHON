# existencia de triangulo e forma 
l1 = float(input('Digite o tamanho do lado 1: '))
l2 = float(input('Digite o tamanho do lado 2: '))
l3 = float(input('Digite o tamanho do lado 3: '))
if l1 < l2 + l3 or l2 < l1 + l3 or l3 < l1 + l2:
    print('Pode formar um triângulo!')
else:
    print('Não pode formar triângulo!')
# Verifica a forma do triângulo
if l1 == l2 and l1 == l3:
    print('Triângulo Equilatero')
elif l1 == l2 or l1 == l3:
    print('Triangulo Isoceles')
else:
    print('Triangulo escaleno')