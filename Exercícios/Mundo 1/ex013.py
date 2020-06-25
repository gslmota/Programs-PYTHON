# Sortear alunos
import random
nome1 = str(input('Digite o nome do aluno: '))
nome2 = str(input('Digite o nome do aluno: '))
nome3 = str(input('Digite o nome do aluno: '))
nome4 = str(input('Digite o nome do aluno: '))
lista = [nome1, nome2, nome3, nome4]
sorteado = random.choice(lista)
print('O escolhido é {}'.format(sorteado))