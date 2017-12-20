import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

print(sqlalchemy.__version__)
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/blog", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def get_info(self):
        return {"id": self.id, "name": self.name, "age": self.age}
