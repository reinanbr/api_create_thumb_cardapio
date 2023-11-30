import requests as req
from datetime import datetime
import pytz

dt_now = datetime.now(pytz.timezone('America/Sao_Paulo'))
data_climate = req.get('https://raw.githubusercontent.com/reinanbr/noawclg/main/data_info/juazeiro_ba.json').json()
 

def get_date_key(dt_now:datetime):
    hours = dt_now.hour
    
    hours_key = 0
    hours_rest = hours%3
    if hours_rest > 1:
        hours_key = ((hours//3)*3)+3
    elif hours_rest==1:
        hours_key = (hours//3)*3
    else:
        hours_key = hours
    
    date_base = datetime(dt_now.year,dt_now.month,dt_now.day,hours_key,0)
    date_key = date_base.strftime("%d/%m/%Y_%H:%M")
    print(date_key)
    return date_key


def get_data_by_date(dt):
    dt_key = get_date_key(dt)
    data_date = data_climate[dt_key]
    return data_date


data_now = (get_data_by_date(dt_now))