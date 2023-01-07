import os
import requests
import time
from dotenv import load_dotenv

class PedidoEletronico:

    def __init__(self):
        load_dotenv()
        token = os.getenv('Token')
        self.headers = {'xToken': token}
        self.url_base = "https://apidata.pedidoeletronico.com/api/"

    def __executar_individual(self, tipo_cadastro, id):

        url = self.url_base + tipo_cadastro + "/ObterRegistro/" + str(id)
        response = requests.request("GET", url, headers=self.headers)

        return response.json()

    def __obter_todos(self, tipo_cadastro):
        lista = []
        finalizado = False
        p = 1
        while not finalizado:
            url = self.url_base + tipo_cadastro + "/ObterRegistros/" + str(p) + "/100/0000-00-00T00:00:00"
            response = requests.request("GET", url, headers=self.headers)
            busca = response.json()
            listagem = busca["ListagemRetorno"]
            if listagem == []:
                finalizado = True
            else:
                for Produto in listagem:
                    lista.append(Produto)
                p += 1
            time.sleep(.6)

        return lista

    def obter_produtos(self): return self.__obter_todos("Produto")
    def obter_tabelas_de_preco(self): return self.__obter_todos("TabelaPreco")
    def obter_estoque_individual(self, id_produto): return self.__executar_individual("Estoque", id_produto)