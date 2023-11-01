from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from fastapi import FastAPI,Request
from fastapi.responses import FileResponse
from pathlib import Path
import datetime as dt
import time
import os

from src.create_template import create_painel_food as cpf
from src.tools.date import get_date_info as gdi


date = gdi()

filename = f'thumb_{date["date"]}_{date["hour"]}.png'


app = FastAPI(debug=True)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/get_thumb')
async def get_image(food_name:str):

    path_img = f"/tmp/test.png"
    print(f'food_name é {food_name}')
    res_cpf = cpf(food_name,path_img)

    # Verifica se o arquivo existe
    arquivo = Path(res_cpf['response'])
    if arquivo.is_file():
        # Retorna o arquivo como resposta
        return FileResponse(res_cpf['response'], filename=filename)
    else:
        return "Arquivo não encontrado", 404





if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run('main:app', host="0.0.0.0", port=port, reload=True)