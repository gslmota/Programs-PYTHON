# Aula de Tratamento de erros e exceções
try:
    a = int(input("Digite um num: "))
    b = int(input('Digite um num'))
    c = a/b
except Exception as erro:
    print(f'Nao funcionou{erro.__class__}')
else:
    print(c)
finally:
    print('Bye Bye')