import pandas as pd
import yfinance as yf

def download_data(symbols):
    """
    Função utilizada para baixar dados do Yahoo Finance (yfinance) e salvar como Parquet (gzip)
    """
    path = '/home/aluno/projeto_ia/data/raw/'

    for symbol in symbols:
        path_full = path+symbol+'.parquet.gzip'
        df = yf.download(symbol,start=start_date, end=end_date)

        if df.shape[0]==0: #Verificar se o DataFrame está vazio
            print(f'A base {symbol} não está disponível')
        else: #Salvar o DataFrame como Parquet
            df.to_parquet(path_full,compression='gzip')
        
symbols = ["BTC-USD","ETH-USD","USDT-USD","SOL-USD","DOGE-USD"] #Simbolos das criptomoedas que serão analisadas
start_date = "2018-01-01"
end_date = "2023-11-29"

download_data(symbols) 

