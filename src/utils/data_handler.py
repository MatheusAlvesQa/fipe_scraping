import pandas as pd
from config.settings import pandas_options 

planilha = "data/result.xlsx"

def armazenar_dados(dados):
    df = pd.read_excel(planilha, **pandas_options)
    novos_dados = pd.DataFrame([dados], columns=pandas_options["usecols"])
    df = pd.concat([df, novos_dados], ignore_index=True)
    df.to_excel(planilha, index=False)