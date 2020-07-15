# Sistema de ajuda em Python
def ajuda(com):
    
#Programa Principal
comando = ''
while True:
    comando = str(input("Função ou Biblioteca: "))
    if comandox.upper() == 'FIM':
        break
    else:
        ajuda(comando)