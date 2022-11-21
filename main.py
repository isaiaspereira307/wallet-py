from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import datetime


def ler_empresas():
    """Ler arquivo xlsx com todas as empresas."""
    ...

def chamar_cotações_das_empresas(ativo: str):
    """Chama a cotação da empresa de acordo com os parametros passados."""
    # data -> MM/DD/AAAA
    data_inicio = '01/01/2022'
    data_final = '11/23/2022'
    source = 'yahoo'
    sigla = f'^{ativo}'
    cotacao = web.DataReader('^BVSP', data_source=source, start='10/01/2022', end='10/23/2022')
    return cotacao


def comparar_empresas():
    """Analisa as 10 melhores empresas."""
    ...



# cotacao_bovespa = web.DataReader('^BVSP', data_source='yahoo', start='10/01/2022', end='10/23/2022')
# # cotacao_magalu = web.DataReader('MGLU.SA', data_source='yahoo', start='10/01/2022', end='10/23/2022')

# ticker = yf.Ticker('PETR4.SA')

# df = ticker.history(period='30d')
# df = df['Close']

# df_ticker_daily = ticker.history(period='1d', interval='5m')
# df_ticker_daily = df_ticker_daily['Close']

# df = pd.DataFrame(df)
# df_ticker_daily = pd.DataFrame(df_ticker_daily)



# cotacao_bovespa['Adj Close'].plot()
# plt.show()


# dataframe1 = pd.read_csv("exemplo.txt")
# # storing this dataframe in a csv file
# dataframe1.to_csv('exemplo.csv', index = None)



# data_inicial = "01/01/2020"
# data_final = "01/01/2021"

# empresas_df = pd.read_excel("Empresas.xlsx")
# empresas_df

# for empresa in empresas_df['Empresas']: 
#     print(f"{empresa}:")
#     df = web.DataReader(f'{empresa}.SA', data_source='yahoo', start=data_inicial, end=data_final)
#     df
#     df["Adj Close"].plot(figsize=(15, 10))
#     plt.show()