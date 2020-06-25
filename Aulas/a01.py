n1 = int(input('Digite um número:'));
n2 = int(input('Digite outro número:'));
soma = n1 + n2;
#print('A soma é: ' + soma); isso tbm funciona print('A soma é:', soma);
print('A soma entre {} e {} vale {}'.format(n1, n2, soma));

txt = input('Digite alguma coisa:');
# O 'is...' serve para exibir informações
print(txt.isalnum);
print(txt.isalpha);
print(txt.islower);
print('testando {:=^20}'.format(txt));