from typing import Optional

from pydantic import BaseModel, validator


class Viagem(BaseModel):
    id: Optional[int] = None
    titulo: str
    dias: int  
    noites: int 

    @validator('titulo')
    def validar_titulo(cls, value: str):
        # Validacao 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras.')

        # Validacao 2
        if value.islower():
            raise ValueError('O título deve ser capitalizado.')

        return value


viagens = [
    Viagem(id=1, titulo='Pacote para França', dias=11, noites=10),
    Viagem(id=2, titulo='Pacote para Bahia', dias=10, noites=9),
]
