from PIL import ImageFont
from PIL import ImageDraw 
from PIL import Image
from src.tools.date import get_date_info, days_new_year
from src.tools.resize_for_text import resize_for_text
from src.tools.get_climate import data_now

path_img = 'src/templates/pt4.png'
date = get_date_info()
font_name = "src/font/roboto/Roboto-Bold.ttf"
font_name_climate = "src/font/roboto/Roboto-Italic.ttf"
font_emoji_dir = 'src/font/Noto_Emoji/static/NotoEmoji-Bold.ttf'
days_year = days_new_year()


def get_emoji_cloud(percent):
    if percent<20:
        return '☀️'
    elif percent >=20 and percent < 40:
        return '🌤'
    elif percent >=40 and percent < 60:
        return '⛅️'
    elif percent >=60 and percent < 80:
        return '🌦'
    elif percent >=80:
        return '🌧'
    


def _create_painel_food_(food_name:str,path:str='test.png'):
    print(f'food name: {food_name}\npath: {path}')
    font_att = ImageFont.truetype(font_name, 55)
    font_date = ImageFont.truetype(font_name, 55)
    font_date_y = ImageFont.truetype(font_name, 70)
    font_climate = ImageFont.truetype(font_name_climate,90)
    font_climate_small = ImageFont.truetype(font_name_climate,55)
    font_emoji = ImageFont.truetype(font_emoji_dir,80)

    font_food_name = ImageFont.truetype("src/font/Courgette-Regular.ttf",95)
    img = Image.open(path_img).convert('RGB')
    draw = ImageDraw.Draw(img)

    draw.text((10, 350),f'Cárdapio atualizado às {date["hour"]}, \ndo dia {date["date"]}','#000',font=font_att)
    draw.text((10, 1315),f'*Sujeito a alterações','#000',font=font_att)
    draw.text((1750,350),f" {date['day_week']}\n{date['date']}",'#000',font=font_date)
    draw.text((1650,50),f"FALTAM\n{days_new_year()} DIAS\nPARA 2024🎉",'#fff',font=font_date_y)
    
    percent_cloud = (data_now['cloud']+data_now['rain_percent'])
    print(percent_cloud)
    draw.text((280,1180),f"Petrolina-PE    {(data_now['temperature']+1.1):.1f}ºC","#000",font=font_climate)
    draw.text((1180,1165),f'Humidade: {data_now["humidity"]:.1f}%','grey',font=font_climate_small)
    draw.text((1180,1225),f'Vento: {(data_now["v"]*3.6):.1f}km/h','grey',font=font_climate_small)
    draw.text((790,1180),get_emoji_cloud(percent_cloud),'#000',font=font_emoji)
    
    x = resize_for_text(food_name)
    draw.text((x,700),food_name,'#000',font=font_food_name)
    
    img.save(path)



def create_painel_food(food_name:str,path:str='test.png'):
    try:
        _create_painel_food_(food_name,path)
        print('succes')
        return {'success':True,
                'response':path}

    except Exception as e:
        pass
        print('not succes')        
        return {'success':False,
                'response':str(e)}
