# Verifica sexo
sexo = 'j'
while sexo != 'M' and  sexo != 'F':  # poderia ser while sexo not in 'MmFf': 
    sexo = str(input('Digite o seu sexo m ou f: ')).strip().upper()
print('Tudo Certo!')