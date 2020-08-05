class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    

    def inserirProduto(self, produto):
        self.produtos.append(produto)


    def listaProdutos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    
    def somaTotal(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return soma

        
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor