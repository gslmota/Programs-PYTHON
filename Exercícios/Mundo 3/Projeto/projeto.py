from lib.interface import *
from lib.arquivo import *
from time import sleep
arquivo = 'projeto.txt'
if not arqExiste(arquivo):
    criarArq(arquivo)

cabecalho('Sistema Arquivo v1.0')
while  True:
    resposta = menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArq(arquivo)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do Sistema!')
        break
    else:
        print('\033[31m ERRO: Por favor digite uma opção válida.\033[m')
        sleep(1)