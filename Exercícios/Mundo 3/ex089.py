from time import sleep
# Função que realiza contagem
def contador(i, f, p):
    if f > i:
        for x in range(i, f, p):
            print(x)
            sleep(0.5)
    else:
        for x in range(i, f, -p):
            print(x)
            sleep(0.5)



# programa principal
ini = int(input('Digite o inicio da contagem: '))
fim = int(input('Digite o final da contagem: '))
pas = int(input('Digite o passo da contagem: '))
contador(ini, fim, pas) 