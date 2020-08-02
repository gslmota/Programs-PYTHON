# Conceito de encapsulamento
class BasedeDados:
    def __init__(self):
        self.dados = {}

    def inserirClientes(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})
            