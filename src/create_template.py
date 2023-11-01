from PIL import ImageFont
from PIL import ImageDraw 
from PIL import Image
from src.tools.date import get_date_info
from src.tools.resize_for_text import resize_for_text

path_img = 'src/templates/pt1.png'
date = get_date_info()
font_name = "src/font/roboto/Roboto-Medium.ttf"


def _create_painel_food_(food_name:str,path:str='test.png'):
    print(f'food name: {food_name}\npath: {path}')
    font_att = ImageFont.truetype(font_name, 55)
    font_date = ImageFont.truetype(font_name, 55)
    font_food_name = ImageFont.truetype("src/font/Courgette-Regular.ttf",90)
    img = Image.open(path_img).convert('RGB')
    # img = img_.resize((496, 323))
    draw = ImageDraw.Draw(img)

    draw.text((10, 350),f'Cárdapio atualizado às {date["hour"]}, \ndo dia {date["date"]}','#000',font=font_att)
    draw.text((10, 1315),f'*Sujeito a alterações','#000',font=font_att)
    draw.text((1750,350),f" {date['day_week']}\n{date['date']}",'#000',font=font_date)
        
    #parte delicada, devido a otamanho que o nome pode ter
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