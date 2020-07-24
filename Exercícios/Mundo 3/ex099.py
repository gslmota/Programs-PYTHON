# Programa que verifica se o site esta acessivel
import urllib
import urllib.request
# Programa principal
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Ocorreu um erro!')
else:
    print('Deu tudo certo!')