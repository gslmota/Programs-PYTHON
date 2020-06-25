# Aumento Salarial
salario = int(input('Digite o seu sálario: '))
if salario > 1200:
    aumento = salario * 0.10
    nsal = salario + aumento
else:
    aumento = salario * 0.15
    nsal = salario + aumento

print('O novo sálario é {}'.format(nsal))