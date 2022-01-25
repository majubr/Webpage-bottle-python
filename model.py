from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String, Integer
from sqlalchemy import create_engine

Base = declarative_base()

class User (Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    nome_usuario = Column (String(30),unique=True, nullable = False)
    senha = Column (String(30),nullable = False)

    def __repr__(self):
        return nome_usuario

engine = create_engine ('sqlite:///database.db')

Base.metadata.create_all (engine)