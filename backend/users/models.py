from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base, engine
from appointments.models import AppointmentModel


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    
    details = relationship('DetailsModel', back_populates="users")
    appointments = relationship('AppointmentModel', back_populates="users", foreign_keys=[AppointmentModel.booked_by_id])
