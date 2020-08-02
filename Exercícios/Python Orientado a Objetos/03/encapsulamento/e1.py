# Conceito de encapsulamento
class BasedeDados:
    def __init__(self):
        self.dados = {}

    def inserirClientes(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})


    def listaClientes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)


    def apagaClientes(self, id):
        del self.dados['clientes'][id]

        