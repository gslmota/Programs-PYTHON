# Nota de Alunos
cores = {'limpa' : '\033[m', 'azul' : '\033[34m', 'vermelho' : '\033[31m', 'amarelo': '\033[33m'}
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    resultado = 'Reprovado'
    print(' Você está {}{}{}'.format(cores['vermelho'], resultado, cores['limpa']))
elif media >= 5 and media <= 6.9:
    resultado = 'Recuperação'
    print('Você está de {}{}{}'.format(cores['amarelo'], resultado, cores['limpa']))
else:
    resultado = "Aprovado"
    print('Você está {}{}{}'.format(cores['azul'], resultado, cores['limpa']))