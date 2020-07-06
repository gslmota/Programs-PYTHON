# função que calcula area de um terreno 
def area(comp, larg):
    area = comp * larg
    print(f'A area é {area}')


#programa principal
c = float(input('Digie o comprimento: '))
l = float(input('Digite a largura: '))
area(c, l)
