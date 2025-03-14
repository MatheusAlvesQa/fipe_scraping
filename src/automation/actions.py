from src.utils import elements as el
import time
from selenium.webdriver.common.keys import Keys

def consulta_fipe(driver):
    driver.find_element("xpath", el.consulta_carro['expandir_campos']).click()
    time.sleep(1)
    driver.find_element("xpath", el.consulta_carro['pesquisa_comum']).click()

def consulta_marca(driver, marca):
    time.sleep(3)
    driver.find_element("xpath", el.consulta_carro['span_marca']).click()
    time.sleep(1)
    driver.find_element("xpath", el.consulta_carro['input_marca']).send_keys(marca, Keys.ENTER)

def consulta_modelo(driver, modelo):
    time.sleep(1)
    driver.find_element("xpath", el.consulta_carro['span_modelo']).click()
    time.sleep(1)
    driver.find_element("xpath", el.consulta_carro['input_modelo']).send_keys(modelo, Keys.ENTER)

def consulta_ano(driver, ano):
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -300);")
    time.sleep(1)
    driver.find_element("xpath", el.consulta_carro['span_ano']).click()
    time.sleep(1)
    driver.find_element("xpath", el.consulta_carro['input_ano']).send_keys(ano, Keys.ENTER)

def listar_modelos(driver):
    time.sleep(1)
    driver.find_element("xpath", el.consulta_carro['span_modelo']).click()
    time.sleep(1)
    lista_modelos = driver.find_elements("xpath", el.consulta_carro['lista_modelos'])
    todos_modelos = [modelo.text for modelo in lista_modelos]
    time.sleep(1)
    driver.find_element("xpath", el.consulta_carro['input_modelo']).send_keys(Keys.ESCAPE)

    return todos_modelos

def listar_ano(driver):
    driver.find_element("xpath", el.consulta_carro['span_ano']).click()
    time.sleep(1)
    lista_anos = driver.find_elements("xpath", el.consulta_carro['lista_ano'])
    todos_anos = [idade.text for idade in lista_anos]
    driver.find_element("xpath", el.consulta_carro['input_ano']).send_keys(Keys.ESCAPE)
    
    return todos_anos

def button_pesquisar(driver):
    driver.find_element("xpath", el.consulta_carro['button_pesquisar']).click()

def button_limpar(driver):
    driver.find_element("xpath", el.consulta_carro['button_limpar_pesquisa']).click()

def dados_pesquisa(driver):
    dados_capturados = []
    get_marca = driver.find_element("xpath", el.resultado_pesquisa['marca'])
    get_fipe = driver.find_element("xpath", el.resultado_pesquisa['fipe'])
    get_ano = driver.find_element("xpath", el.resultado_pesquisa['ano'])
    get_modelo = driver.find_element("xpath", el.resultado_pesquisa['modelo'])
    get_valor = driver.find_element("xpath", el.resultado_pesquisa['valor'])
    
    dados_capturados.extend([
        get_marca.text,
        get_fipe.text,
        get_ano.text,        
        get_modelo.text,
        get_valor.text
        ])

    return dados_capturados