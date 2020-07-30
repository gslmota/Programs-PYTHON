import random
class Pessoa:
    ano_atual = int(datetime.strptime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo = False, falando = False):
       self.nome = nome
       self.idade = idade
       self.comendo = comendo
       self.falando = falando


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome}não pode falar comendo!')
            return
        if self.falando:
            print(f'{self.nome} já está falando sobre {assunto}!')
            self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return
        
        print(f'{self.nome} está comendo {alimento}!')
        self.comendo = True

        if self.falando:
            print(f'{self.nome} não pode comer falando!')
            return 


    def parar_de_comer(self): # <- é um metodo de instancia
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


    @classmethod  #<-  é referente a classe em si
    def por_ano_nascimento(cls, nome,ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    

    @staticmethod #<- refere tanto a classe, tanto como uma função normal
    def gera_id():
        n = random.randint(1000, 1900)
        return n
