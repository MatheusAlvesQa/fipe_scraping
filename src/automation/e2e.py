from src.automation import actions
from src.utils import data_handler
import time

def preparando_consulta(driver):
    actions.consulta_fipe(driver)
    actions.consulta_marca(driver, "Fiat")
    lista_modelos = actions.listar_modelos(driver)

    return lista_modelos

def buscando_resultado(driver, modelos):
    while(modelos):
        actions.consulta_modelo(driver, modelos[0])
        lista_anos = actions.listar_ano(driver)
        print(lista_anos)
        armazenando_dados(driver, lista_anos)
        del modelos[0]
        time.sleep(2)
        actions.button_limpar(driver)
        actions.consulta_marca(driver, "Fiat")

def armazenando_dados(driver, anos):
    while(anos):
        actions.consulta_ano(driver, anos[0])
        actions.button_pesquisar(driver)
        dados = actions.dados_pesquisa(driver)
        data_handler.armazenar_dados(dados)
        del anos[0]