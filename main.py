from src.automation import browser, actions, e2e
from src.utils import data_handler
def abrir_chrome():
    driver = browser.iniciando_chromedriver()
    return driver
    

def main():
    driver = abrir_chrome()
    modelos = e2e.preparando_consulta(driver)
    e2e.buscando_resultado(driver, modelos)


if __name__ == '__main__':
    main()