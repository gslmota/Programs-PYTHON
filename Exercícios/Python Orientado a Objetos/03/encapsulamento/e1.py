# Conceito de encapsulamento
class BasedeDados():
    def __init__(self):
        self._dados = {}


    @property
    def dados(self):
        
    def inserirClientes(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id: nome})


    def listaClientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)


    def apagaClientes(self, id):
        del self._dados['clientes'][id]

        