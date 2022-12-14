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
    appointment_slot : str
    class Config:
        orm_mode = True

class NullResponseModel(BaseModel):
    data: List[None]
    class Config:
        orm_mode = True


class BookAppointment(BaseModel):
    appointment_id: int
    appointment_date : date
    is_booked: bool
    doctor_id: int
    previous_appointment_id: None | int = None
    class Config:
        orm_mode = True