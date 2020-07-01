# Cadastro e situação de aluno usando dicionarios
aluno = {}
nome = str(input('Digite o nome do aluno: '))
media = float(input('Digite a media do aluno: '))
nome.append(aluno)
media.append(aluno)
if media < 7:
    situação = 'Reprovado'
    situação.append(aluno)
else: 
    situação = 'Aprovado'
    situação.append(aluno)
print(aluno)