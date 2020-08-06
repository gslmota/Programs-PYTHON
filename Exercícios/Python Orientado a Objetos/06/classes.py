class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
    

    def inserirEndereco(self, cidade, estado):
        self.enderecos.append()