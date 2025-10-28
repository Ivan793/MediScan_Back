# app/schemas/rol.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RolBase(BaseModel):
    nombre: str
    activo: bool = True

class RolCreate(RolBase):
    pass

class RolUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    activo: Optional[bool] = None

class RolResponse(RolBase):
    id_rol: str
    creado_en: datetime
    actualizado_en: datetime

    class Config:
        from_attributes = True
