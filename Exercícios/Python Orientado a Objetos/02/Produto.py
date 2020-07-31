class Produto:
    def __init__(self, name, preco):
      self.name = name
      self.preco = preco

    
    def desconto(self, percentual):
        self.preco = self.preco - ((self.preco * percentual) / 100)


    #getter
    @property
    def preco(self):
        return self._preco


    #setter



# classe main
p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)