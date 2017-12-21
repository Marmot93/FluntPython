import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker

# setting
print(sqlalchemy.__version__)
engine = sqlalchemy.create_engine("postgresql://postgres:postgres@localhost/blog", echo=True)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


# --------------------------
# 查询
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(32))
    age = Column(Integer)

    def get_info(self):
        return {"id": self.id, "name": self.name, "age": self.age}


our_user = session.query(User).order_by(User.id)
for _ in our_user:
    print(_.get_info())
