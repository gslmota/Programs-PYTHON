# Usando moeda
from utilidades import moeda
from utilidades import dado
p = dado.leiaDinheiro('Digite o preço:R$')
moeda.resumo(p, 35, 22)