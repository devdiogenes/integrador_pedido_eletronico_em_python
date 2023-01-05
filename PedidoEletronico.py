import os
import requests
import time
from dotenv import load_dotenv

class PedidoEletronico:

    def listar_produtos(self):
        lista = []
        finalizado = False
        p = 1
        while finalizado == False:
            busca = self.__executar("Produto", pagina = p)
            listagem = busca["ListagemRetorno"]
            if listagem == []:
                finalizado = True
            else:
                for Produto in listagem:
                    lista.append(Produto)
                p += 1
            time.sleep(.6)

        return lista

    def __executar(self, tipo_cadastro, pagina = 1, qtd_por_pagina = 100):
        load_dotenv()
        Token = os.getenv('Token')
        headers = {
        'xToken': Token
        }
        url = "https://apidata.pedidoeletronico.com/api/" + tipo_cadastro + "/ObterRegistros/" + str(pagina) + "/" + str(qtd_por_pagina) + "/0000-00-00T00:00:00"
        response = requests.request("GET", url, headers=headers)

        return response.json()