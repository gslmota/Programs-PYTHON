# pintando parede
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digie a altura da parede: '))
area = largura * altura
quantidadeTinta = area / 2
print('Para pintar {} metros quadrados, é necessário {} litros de tinta.'.format(area, quantidadeTinta))