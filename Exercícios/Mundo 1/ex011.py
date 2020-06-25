# medidas da hipotenusa
import math
coposto = float(input('Digite a medida do cateto oposto: '))
cadjacente = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = math.hypot(coposto,cadjacente) 
print('A medida da hipotenusa é {}'.format(hipotenusa))