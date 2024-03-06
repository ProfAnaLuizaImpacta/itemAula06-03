from typing import Dict, List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends

from time import sleep

from models import Viagem
from models import viagens


def banco_mocado():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)


app = FastAPI(
    title='API de Viagens de treino',
    version='0.0.1',
    description='Uma API para estudo do FastAPI'
)


@app.get('/viagens',
         description='Retorna todas os Viagens ou uma lista vazia.',
         summary='Retorna todas os Viagens',
         response_model=List[Viagem],
         response_description='Viagens encontrados com sucesso.')
async def get_Viagens(db: Any = Depends(banco_mocado)):
    return viagens


@app.post('/viagens', status_code=status.HTTP_201_CREATED, response_model=Viagem)
async def post_viagem(viagem: Viagem):
    next_id: int = len(viagens) + 1
    viagem.id = next_id
    viagens.append(viagem)

    return viagem


@app.put('/viagens/{viagem_id}', status_code=status.HTTP_204_NO_CONTENT)
async def put_viagem(viagem_id: int, viagem: Viagem, db: Any = Depends(banco_mocado)):
    if viagem_id in viagens:
        Viagens[viagem_id] = viagem
        del viagem.id

        return viagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um viagem com id {viagem_id}')


@app.delete('/viagens/{viagem_id}')
async def delete_viagem(id: int, db: Any = Depends(banco_mocado)):
    if id in viagens:
        del viagens[id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe um viagem com id {id}')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
