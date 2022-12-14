from sqlalchemy.orm import Session
from datetime import date
from .models import AppointmentModel
from utils import commit_refresh


def filter_appointments_by_doctor_and_date(db: Session, appointment_date: date, doctor_id: int):
    return db.query(AppointmentModel).filter(AppointmentModel.doctor_id==doctor_id, AppointmentModel.appointment_date==appointment_date, AppointmentModel.is_booked==False).all()


def change_booking_status(db: Session, appointment_id: int, previous_appointment_id: int = None):
    if previous_appointment_id:
        print(previous_appointment_id)
    result =  db.query(AppointmentModel).filter(AppointmentModel.id==appointment_id).one()
    result.is_booked = not(result.is_booked)
    commit_refresh(db, result)
    return result