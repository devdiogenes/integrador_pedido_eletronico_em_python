# Integração Pedido Eletrônico em Python
Uma maneira fácil de comunicar-se com a API do PedidoEletronico, sistema de vendas brasileiro, utilizando Python. Obtenha diversos métodos pré configurados, utilizando apenas uma classe. 

## Configuração inicial

### Primeiramente, crie um arquivo .env contendo os seguintes dados: 

*Token = 'seu token aqui'*

### Após, instale as bibliotecas necessárias, rodando dentro dessa pasta o comando:

*pip install -r requirements.txt*<br>

### E então, você pode usar o arquivo *exemplo.py* para entender como essa biblioteca funciona, e se basear.

## Métodos já configurados: 

+ **PedidoEletronico()**.obter_estoque_individual(id_produto)
+ **PedidoEletronico()**.obter_produtos()
+ **PedidoEletronico()**.obter_tabelas_de_preco()