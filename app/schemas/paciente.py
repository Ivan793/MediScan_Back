# app/schemas/paciente.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class PacienteBase(BaseModel):
    nombre: str
    identificacion: str
    fecha_nacimiento: date
    activo: bool = True

class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    nombre: Optional[str] = None
    identificacion: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    activo: Optional[bool] = None

class PacienteResponse(PacienteBase):
    id_paciente: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

