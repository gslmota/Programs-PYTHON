# Sortear ordem de apresentação
import random
nome1 = str(input('Digite o nome do aluno: '))
nome2 = str(input('Digite o nome do aluno: '))
nome3 = str(input('Digite o nome do aluno: '))
nome4 = str(input('Digite o nome do aluno: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem de apresentação é {}'.format(lista))