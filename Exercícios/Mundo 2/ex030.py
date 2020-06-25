# Empréstimo Bancário
vcasa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
tpag = int(input('Digite em quantos anos vai pagar a casa: '))
porsal = sal * 0.3
prest =vcasa/(tpag*12)
print('Para pagar uma casa de {} reais em {}anos. O valor da prestação será de {:0.2f} reais.'.format(vcasa, tpag, prest))
if prest > porsal:
    print('Emprestimo negado!')
else :
    print('Emprestimo aprovado!')
