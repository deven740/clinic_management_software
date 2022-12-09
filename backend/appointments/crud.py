from sqlalchemy.orm import Session
from datetime import date
from .models import AppointmentModel


def filter_appointments_by_doctor_and_date(db: Session, appointment_date: date, doctor_id: int):
    return db.query(AppointmentModel).filter(AppointmentModel.doctor_id==doctor_id, AppointmentModel.appointment_date==appointment_date).all()