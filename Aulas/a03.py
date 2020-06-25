#String
# Análise em Strings
frase = 'Olá Mundo!'
print(frase[2]) # mostra á
print(frase[2:5]) # mostra do á até M, excluindo o u.
print(frase[1:7:2]) # mostra do 1 até o 7 pulando de 2 em 2.
print(frase[:5]) # Vai do inicio até o 5.
print(frase[2:]) # vai do 2 até o final.
print(frase[2::3]) # Vai do 2 até o final pulando de 3 em 3.
print(len(frase)) # retorna o tamanho da frase.
print(frase.count('o')) # conta quantas vezes aparece o (o).
print(frase.count('o,0,5')) # conta quantas vezes aparece o (o) entre 0 e 5.
print(frase.find('lá')) # mostra quantas vezes encontrou o lá na string. quanado n encontra a string ele retorna -1.
print('Mundo!' in frase) # mostra true na tela pois existe.

# Transformação em Strings
frase.replace('Olá', 'Bom dia') # troca o olá por bom dia na string.
frase.upper() # coloca em maisculas
frase.lower() # coloca em minusculas
frase.capitalize() # coloca tudo em minusculas exceto a primeira letra.
frase.title() # coloca tudo depois dos espaços como maiusculas.
frase.strip() # remove todos os espaços inúteis (excedentes) string. 
frase.rstrip() # remove apenas os espaços da direita. 
frase.lstrip() # remove apenas os espaços da esquerda. 

# Divisão em Strings
frase.split() # pega onde tem espaços e faz uma divisão, criando novas strings em uma lista. ver foto
'-'.join(frase) # pega a string dividida e faz a junção dela, colocando um - entre cada uma delas. 
# print(""" fnjkbfsjbjbsbafsjfbsjfbsjbfjsbfjsbsbd
# sjfbjsbfsjbfsbfjsbfsbfsjfsjabfjfjsfbjsbf""") serve para printar um texto grande.
# você não pode fazer uma alteração direta em uma string EX: frase[0] = 'B'. <- não pode fazer isso.