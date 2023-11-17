from PIL import ImageFont
from PIL import ImageDraw 
from PIL import Image
from src.tools.date import get_date_info, days_new_year
from src.tools.resize_for_text import resize_for_text

path_img = 'src/templates/pt4.png'
date = get_date_info()
font_name = "src/font/roboto/Roboto-Bold.ttf"
days_year = days_new_year()


def _create_painel_food_(food_name:str,path:str='test.png'):
    print(f'food name: {food_name}\npath: {path}')
    font_att = ImageFont.truetype(font_name, 55)
    font_date = ImageFont.truetype(font_name, 55)
    font_date_y = ImageFont.truetype(font_name, 75)
    font_food_name = ImageFont.truetype("src/font/Courgette-Regular.ttf",90)
    img = Image.open(path_img).convert('RGB')
    draw = ImageDraw.Draw(img)

    draw.text((10, 350),f'Cárdapio atualizado às {date["hour"]}, \ndo dia {date["date"]}','#000',font=font_att)
    draw.text((10, 1315),f'*Sujeito a alterações','#000',font=font_att)
    draw.text((1750,350),f" {date['day_week']}\n{date['date']}",'#000',font=font_date)
    draw.text((1650,50),f"FALTAM\n{days_new_year()} DIAS\nPARA 2024🎉",'#fff',font=font_date_y)
    
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
        return {'success':True,
                'response':str(e)}
