from fastapi import FastAPI, Depends, HTTPException
from models import Base, Tarefa
from schemas import TarefaSchema
from database import engine,SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
async def home():
    return {"message": "Hello, World!"}

@app.post("/addtarefa")
async def add_tarefa(request:TarefaSchema, db: Session = Depends(get_db)):
    tarefa = Tarefa(id=request.id, item=request.item)
    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)
    return tarefa

@app.get("/tarefa/{tarefa_name}")
async def get_tarefas(tarefa_n0me,db: Session = Depends(get_db)):
    tarefas= db.query(Tarefa).filter(Tarefa.item == tarefa_nome).first()
    return tarefas


    import uvicorn
