from PedidoEletronico import *

exemplo = PedidoEletronico()
lista_de_produtos = exemplo.obter_produtos()

for produto in lista_de_produtos:
    print(produto['xNome'])