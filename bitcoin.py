#!/usr/bin/env python3

import json
import requests
import argparse


def get(url: str):
    response = requests.request("GET", url)

    return response.text


def cotacaoBRL() -> float:
    """
    Retorna a última cotação do Bitcoin em BRL - Mercado Bitcoin via API BitValor
    """
    dados = get(url="https://api.bitvalor.com/v1/ticker.json")
    data = json.loads(dados)
    last: float = data['ticker_24h']['exchanges']['MBT']['last']
    return last


def cotacaoUSD():
    """
    Retorna a última cotação do Bitcoin em USD - API Bitfinex
    """
    dados = get(url="https://api.bitfinex.com/v1/pubticker/btcusd")
    data = json.loads(dados)
    last: float = data['last_price']
    return last


def btc2brl(btc: float):
    """
    Recebe uma quantidade de BTC como parâmetro e retorna seu valor aproximado em Real
    """
    price = cotacaoBRL()
    brl = price * btc
    brl = "{0:.2f}".format(brl)

    return brl


def btc2usd(btc: float):
    """
    Recebe uma quantidade de BTC como parâmetro e retorna seu valor aproximado em USD
    """

    price = cotacaoUSD()
    usd = price * btc
    usd = "{0:.2f}".format(usd)

    return usd


import sys

btc = ''

if len(sys.argv)>0:
    sys.argv.pop(0)
    btc = ' '.join(sys.argv).replace(',','.')

if not btc:
    print("\nModo de uso:\n\n./bitcoin [unidade]\n\nExemplos:\n\n./bitcoin 0.35 (para Bitcoin)\n./bitcoin R100 (para Real)\n./bitcoin U100 (para Dólar)\n./bitcoin C (para consultar a cotação atual)\n\n")

elif (btc[0].upper()=='U'):
    usd = float(btc[1:])
    value = usd/float(cotacaoUSD())
    print(value)

elif (btc[0].upper()=='R'):
    brl = float(btc[1:])
    value = brl/float(cotacaoBRL())
    print(value)

elif (btc[0].upper()=='C'):
    print('USD: %s | BRL: %s' %(cotacaoUSD(), cotacaoBRL()))

elif float(btc):
    btc = float(btc)
    print("R$\t", btc2brl(btc)) 
    print("USD\t", btc2usd(btc)) 


parser = argparse.ArgumentParser(
    prog="exceltool",
    description='Excel Tool',
    epilog="Author: Isaías Pereira",
    usage="%(prog)s [options]"
)

parser.version = "exceltool cli 1.0.0"
parser.add_argument('-v', '--version', action="version")
parser.add_argument('-u', '-U', type=str, help='pega valor em Dólar')
parser.add_argument('-r', '-R', type=str, help='pega valor em Real')
parser.add_argument('-c', '-C', type=str, help='pega cotação atual btc')
parser.add_argument('-v', '-V', type=str, help='pega valor em btc')


args = parser.parse_args()

if __name__ == '__main__':
    if args.u:
        usd = float(args.u)
        value = usd/float(cotacaoUSD())
        print(value)
    elif args.r:
        brl = float(args.r)
        value = brl/float(cotacaoBRL())
        print(value)
    elif args.c:
        print('USD: %s | BRL: %s' %(cotacaoUSD(), cotacaoBRL()))
    elif args.v:
        btc = float(args.v)
        print("R$\t", btc2brl(btc)) 
        print("USD\t", btc2usd(btc))
