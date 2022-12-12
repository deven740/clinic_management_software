# from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from . import crud
from .schemas import FilterAppointment, AppointmentResponseModel, BookAppointment


router = APIRouter(
    prefix="/appointments",
    tags=["appointments"]
)


@router.post("/filter-appointments-by-doctor-and-date", response_model=List[AppointmentResponseModel])
def filter_appointments_by_doctor_and_date(data: FilterAppointment, db: Session = Depends(get_db)):
    appointments = crud.filter_appointments_by_doctor_and_date(db, data.appointment_date, data.doctor_id)
    return appointments


@router.post("/book")
def book(data: BookAppointment, db: Session = Depends(get_db)):
    appointments = crud.change_booking_status(db, data.appointment_id, data.previous_appointment_id)
    return appointments