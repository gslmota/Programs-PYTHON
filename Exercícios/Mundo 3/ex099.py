# Programa que verifica se o site esta acessivel
import urllib
import urllib.request
# Programa principal
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Ocorreu um erro! O site não esta acessível!')
else:
    print('Deu tudo certo! O site está acessível!')