# multa de carro
vel = int(input('Digite a velocidade do carro: '))
if vel > 80 :
    exvel = vel - 80
    multa = exvel * 7
    print('Você ultrapassou a velocidade permitida em {} KM/H'.format(exvel))
    print('Você foi multado em {} reais!'.format(multa))