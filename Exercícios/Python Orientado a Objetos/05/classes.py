class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
    

    def inserirProduto(self, produto):
        self.produtos.append(produto)


    def listaProdutos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)
class Produto:
    pass