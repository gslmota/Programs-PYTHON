class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def falar(self):
        print(f'{self.nome} está falando!')


class Cliente(Pessoa):
    pass


class Aluno(Pessoa):
    pass