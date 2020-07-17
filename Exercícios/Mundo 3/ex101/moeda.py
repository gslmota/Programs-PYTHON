# Estudo de Modularização
def aumentar(preco, taxa, format = False):
    res = preco + (preco * taxa)/100
    return res if format is False else moeda(res)


def diminuir(preco, taxa, format = False):
    res = preco - (preco * taxa)/100
    return res if format is False else moeda(res)
    

def dobro(preco, format = False):
    res = preco * 2
    return res if format is False else moeda(res)

    
def metade(preco, format = False):
    res = preco / 2
    return res if format is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco = 0, taxaa = 10, taxar = 5):
    print('-' * 30)
    print('Resumo do Valor')
    print('-' * 30)