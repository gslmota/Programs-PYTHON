class Produto:
    def __init__(self, name, preco):
      self.name = name
      self.preco = preco

    
    def desconto(self, percentual):
        self.preco = self.preco - ((self.preco * percentual) / 100)


# 