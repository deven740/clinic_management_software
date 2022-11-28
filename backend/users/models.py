from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, engine


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role_id  = Column(Integer, ForeignKey("roles.id"))


class RoleModel(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, unique=True, nullable=False)
    user = relationship('UserModel')



Base.metadata.create_all(bind=engine)