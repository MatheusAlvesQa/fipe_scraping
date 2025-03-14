# URL tabela fipe
url = 'https://veiculos.fipe.org.br/'


# Options do driver
uc_options = {
    "headless": False,
    "disable notifications": True,
    "start maximized": True
}


# Options do pandas
pandas_options = {
    "usecols": ["MARCA", "FIPE", "ANO", "MODELO", "VALOR"]
}