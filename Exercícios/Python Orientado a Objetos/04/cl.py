class Escritor:
    def __init__(self, nome):
        self.__nome = nome


    @property
    def nome(self):
        return self.__nome


class Caneta:
    