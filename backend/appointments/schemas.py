from pydantic import BaseModel
from datetime import date
from typing import List


class FilterAppointment(BaseModel):
    appointment_date : date
    doctor_id : int

    class Config:
        orm_mode = True


class AppointmentResponseModel(BaseModel):
    id: int
    appointment_date : date
    appointment_slot : str
    is_booked: bool

    class Config:
        orm_mode = True


class NullResponseModel(BaseModel):
    data: List[None]

    class Config:
        orm_mode = True