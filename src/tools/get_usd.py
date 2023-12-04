import requests as req


def get_brl(minutes=1440):
    data_usd = req.get(f'https://api-forex-py.vercel.app/usd?minutes={minutes}').json()

    data_usd_brl = data_usd['dolar']['now_time']['BRL']
    print(data_usd_brl)
    return data_usd_brl


