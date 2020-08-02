from e1 import BasedeDados
bd = BasedeDados()
bd.inserirClientes(1, 'gabriel')
bd.inserirClientes(4, 'ilda')
bd.inserirClientes(2, 'jorge')
print(bd.dados)
bd.apagaClientes(2)
bd.listaClientes()