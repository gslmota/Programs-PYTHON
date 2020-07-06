# Exercicio de print especial
def pmsg(msg):
    c = len(msg)
    n = '-' * c
    print(n)
    print(msg)
    print(n)

# Programa Principal
strin = str(input('Digite a mensagem: '))
pmsg(strin)