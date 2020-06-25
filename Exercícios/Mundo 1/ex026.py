# Ano bissexto
from datetime import date
print('Para analisar o ano atual digite apenas 0!')
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')


