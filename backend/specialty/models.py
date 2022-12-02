from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, engine


class SpecialtyModel(Base):
    __tablename__ = 'specialty'

    id = Column(Integer, primary_key=True, index=True)
    specialty = Column(String, unique=True, nullable=False)