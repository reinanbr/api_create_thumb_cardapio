import requests as req


def get_brl():
    data_usd = req.get('https://api-forex-py.vercel.app/usd?minutes=60').json()

    data_usd_brl = data_usd['dolar']['now_time']['BRL']

