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


    @property
    def name(self):
        return self._name


    #setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor



    @name.setter
    def name(self, valor):
        self._name = valor



