import undetected_chromedriver as uc
from config import settings

def iniciando_chromedriver():
    options = uc.ChromeOptions()

    if settings.uc_options['headless']:
        options.add_argument("--headless")
    
    if settings.uc_options['disable notifications']:
        options.add_argument("--disable-notifications")

    driver = uc.Chrome(options=options)

    driver.get(settings.url)
    if settings.uc_options['start maximized']:
        driver.maximize_window()

    return driver