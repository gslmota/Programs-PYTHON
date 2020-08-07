class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeClasse} está falando!')


class Cliente(Pessoa):
    pass


class Aluno(Pessoa):
    pass