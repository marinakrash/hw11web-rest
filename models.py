from sqlalchemy import Column, Integer, String,  Table
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Contacts(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, )
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(Integer, nullable=False)
    created_at = Column( DateTime, nullable=False)
    notes = Column(String(150))


