# app/schemas/radiografia.py
from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class RadiografiaBase(BaseModel):
    id_paciente: str
    url_imagen: HttpUrl
    fecha: datetime
    activo: bool = True

class RadiografiaCreate(RadiografiaBase):
    pass

class RadiografiaUpdate(BaseModel):
    url_imagen: Optional[HttpUrl] = None
    fecha: Optional[datetime] = None
    activo: Optional[bool] = None

class RadiografiaResponse(RadiografiaBase):
    id_radiografia: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
