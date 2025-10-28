# app/schemas/paciente.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

from app.schemas.enums.estado_civil import EstadoCivilEnum
from app.schemas.enums.tipo_sangre import TipoSangreEnum
from app.schemas.persona import PersonaBase

class PacienteBase(PersonaBase):
    tipo_sangre: TipoSangreEnum
    profesion: Optional[str]
    estado_civil: EstadoCivilEnum

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

