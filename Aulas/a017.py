# Aula de Tratamento de erros e exceções
try:
    a = int(input("Digite um num: "))
    b = int(input('Digite um num'))
    c = a/b
except:
    print('Nao funcionou')
else:
    print(c)