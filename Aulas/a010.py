# Aula de Tuplas (Variáveis COmpostas)
# Uma Tupla é Imutável
lanche = ('Hamburguer', 'Suco', 'Pudim', 'Pizza')
print(lanche)
print(lanche[1]) # mostra Suco na Tela.
print(lanche[2:3])# Mostra do 2 até o 3 ignorando o 3.
print(sorted(lanche)) # Coloca em ordem
del(lanche) # apaga da memoria
a = (1,2,3)
b = (4,5,6)
c= a + b
print(c)
print(c.count(5)) # Mostra quantas vezes aparece o 5
print(c.index(3)) # Mostra a posição em que está o 3
print(c.index(2, 4)) # Mostra a posição do 2 se houver outro a partir da posição 4
# Uma tupla aceita nomes e numeros ex: a = ('pedro', 10, 23.4)