from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

cotacao_bovespa = web.DataReader('^BVSP', data_source='yahoo', start='10/01/2022', end='10/23/2022')
# cotacao_magalu = web.DataReader('MGLU.SA', data_source='yahoo', start='10/01/2022', end='10/23/2022')

ticker = yf.Ticker('PETR4.SA')

df = ticker.history(period='30d')
df = df['Close']

df_ticker_daily = ticker.history(period='1d', interval='5m')
df_ticker_daily = df_ticker_daily['Close']

df = pd.DataFrame(df)
df_ticker_daily = pd.DataFrame(df_ticker_daily)



cotacao_bovespa['Adj Close'].plot()
plt.show()
