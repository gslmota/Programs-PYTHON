 # Desafio 4 Aula 6
 # Mostra informações sobre o tipo prmitivo
txt = input('Digite alguma coisa: ');
print('O tipo primitivo de {} é {}'.format(txt, type(txt)));
print('Só tem espaços? {}'.format(txt.isspace));
print('É um número? {}'.format(txt.isnumeric));
print('É alfabético? {}'.format(txt.isalpha));
print('É alfanumérico? {}'.format(txt.isalnum));
print('Está em letras maiúsculas? {}'.format(txt.isupper));