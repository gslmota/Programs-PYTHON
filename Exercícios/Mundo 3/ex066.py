# Listagem de produtos com seus preços
produtos = ('Pão', 1, 'Leite', 3, 'Queijo', 20, 'Rosca', 2, 'Picolé', 4, 'Refrigerante', 2.50, 'Pastel', 5)
print('LISTAGEM DE PREÇOS')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end = '')
    else:
        print(f'{produtos[pos]:>7}')

