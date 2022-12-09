from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship

from database import Base


class AppointmentModel(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, index=True)
    appointment_date = Column(Date, nullable=False)
    appointment_slot = Column(String(25), nullable=False)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    booked_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    is_booked = Column(Boolean, default=False)

    users = relationship("UserModel", back_populates="appointments", foreign_keys=[booked_by_id])