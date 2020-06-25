# Estastícas de Produtos
total = tom = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    cont += 1
    total += preco
    if preco > 1000:
        tom += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor =  preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()
        if resp == 'N':
            break
print('{:-^40}'.format('Fim!!!'))
print(f'O total da compra foi {total:10.2f}')
print(f'Total de produtos com valor acima de 1000 {tom}')
print(f'O produto mais barato é {barato} e custa {menor}')
