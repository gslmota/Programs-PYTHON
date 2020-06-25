# Alistamento
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
if idade == 18:
    print('Esta na hora de se alistar!')
elif idade < 18:
    print('Voce ainda não pode se alistar!')
else:
    print('Voce ja passou da idade de se alistar!')
