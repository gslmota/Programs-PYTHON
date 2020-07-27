# class
class Computador:
    def __init__(self,nmarca, nmemoria, nplaca):
        self.marca = nmarca
        self.memoria = nmemoria
        self.placa = nplaca
    pass

computador1 = Computador('Acer', '8gb', 'AMD')
computador2 = Computador('Asus', '16g', 'NVIDIA')
print(computador1.marca, computador1.memoria, computador1.placa)
