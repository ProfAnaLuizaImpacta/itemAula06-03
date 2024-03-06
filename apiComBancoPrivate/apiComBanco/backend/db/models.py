from sqlalchemy import Column, Integer, String
from database import Base

#cria o a tabela tarefas
class Tarefa(Base):
    __tablename__ = "tarefas "

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)


#arquivo 2