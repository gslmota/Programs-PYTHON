# class
class Computador:
    def __init__(self,nmarca, nmemoria, nplaca):
        self.marca = nmarca
        self.memoria = nmemoria
        self.placa = nplaca
    pass
    def ligar(self):
        print('Ligando')
    
    def desligar(self):
        print('Desligando')

    def exibirInfo(self):
        print(self.marca, self.memoria, self.placa)

computador1 = Computador('Acer', '8gb', 'AMD')
computador2 = Computador('Asus', '16g', 'NVIDIA')
print(computador1.marca, computador1.memoria, computador1.placa)
print(computador2.marca, computador2.memoria, computador2.placa)
computador1.ligar()
computador1.exibirInfo()
computador1.desligar()