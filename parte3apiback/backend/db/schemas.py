from pydantic import BaseModel

class TarefaSchema(BaseModel):
    id: int
    item: str


#arquivo 3
