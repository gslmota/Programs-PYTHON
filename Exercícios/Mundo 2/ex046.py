# Verifica os dados
smid = 0
mid = 0
cm = 0
maid = 0
for c in range(0,4):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo f ou m: ')).strip()
    smid += idade
    if sexo == 'm':
        if idade > maid:
            maid = idade
            nm = nome
    else :
        if idade < 20 :
            cm += 1
mid = (smid) / 4
print ('A média das idades é {} '.format(mid))
print ('O nome do homem de maior idade é: {}'.format(nm))
print('Existem {} mulheres com menos de 20 anos'.format(cm))
