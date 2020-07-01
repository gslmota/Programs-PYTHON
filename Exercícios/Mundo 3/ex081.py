# Cadastro e situação de aluno usando dicionarios
aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a media do aluno: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'O aluno {aluno["nome"]} tem media {aluno["media"]} e sua situação é {aluno["situação"]}!')