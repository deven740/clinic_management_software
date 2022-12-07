from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, engine
from users.models import UserModel
from sqlalchemy.ext.hybrid import hybrid_property

class SpecialtyModel(Base):
    __tablename__ = 'specialty'

    id = Column(Integer, primary_key=True, index=True)
    specialty = Column(String, unique=True, nullable=False)


class RoleModel(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, unique=True, nullable=False)


class DetailsModel(Base):
    __tablename__ = 'details'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role_id  = Column(Integer, ForeignKey("roles.id"), nullable=False)
    specialty_id = Column(Integer, ForeignKey('specialty.id'), nullable=True)

    users = relationship("UserModel", back_populates="details")
    
    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name