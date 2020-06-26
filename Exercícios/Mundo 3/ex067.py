# Verifica vogais em tuplas
palavras = ('python', 'casa', 'papel', 'hoje', 'ana', 'luan', 'gabriel', 'macaco', 'peixe', 'aranha')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end = '')
    for let in p:
        if let.lower() in 'aeiou':
            print(let, end = '')