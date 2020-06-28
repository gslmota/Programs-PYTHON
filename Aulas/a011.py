# Aula de Variáveis Compostas [Listas]
num = [1, 2, 3, 4, 5, 6]
print(num)
num [2] = 45
print(num)
num.append(7) # adiciona o 7
num.sort() # ordena
num.sort(reverse = True) # ordena em ordem decrescente
print(num)
num.insert(2, 1) # na posição 2 ele adiciona o valor 1 É possivel trocar valores tbm, usando essa função
num.pop() # remove o ultimo elemento
num.pop(2) # remove o elemento da posição 2
num.remove(4) # remove o 4 da lista, se houver mais de 1, ele remove apenas a primeira ocorrencia



valores = [] # cria uma lista vazia
valores.append(4)
valores.append(8)
valores.append(3)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor: {v}...')


a = [3, 2, 4]
b = a # faz uma ligação de b com a , para fazer copia seria b = a[:] 
# ^ toda alteração feita na lista a ou b em uma ligação altera a outra lista tambem


 

