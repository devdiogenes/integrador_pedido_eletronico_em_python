import os
import requests
import time
from dotenv import load_dotenv

class PedidoEletronico:

    def __init__(self):
        load_dotenv()
        token = os.getenv('Token')
        self.headers = {
        'xToken': token
        }
        self.url_base = "https://apidata.pedidoeletronico.com/api/"

    def listar_produtos(self):
        lista = []
        finalizado = False
        p = 1
        while finalizado == False:
            busca = self.__executar_todos("Produto", pagina = p)
            listagem = busca["ListagemRetorno"]
            if listagem == []:
                finalizado = True
            else:
                for Produto in listagem:
                    lista.append(Produto)
                p += 1
            time.sleep(.6)

        return lista

    def obter_estoque(self, id_produto):
        return self.__executar_individual("Estoque", id_produto)

    def __executar_individual(self, tipo_cadastro, id):

        url = self.url_base + tipo_cadastro + "/ObterRegistro/" + str(id)
        response = requests.request("GET", url, headers=self.headers)

        return response.json()

    def __executar_todos(self, tipo_cadastro, pagina = 1, qtd_por_pagina = 100):
        
        url = self.url_base + tipo_cadastro + "/ObterRegistros/" + str(pagina) + "/" + str(qtd_por_pagina) + "/0000-00-00T00:00:00"
        response = requests.request("GET", url, headers=self.headers)

        return response.json()