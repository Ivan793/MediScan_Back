# app/schemas/reporte.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReporteBase(BaseModel):
    id_doctor: str
    id_paciente: str
    id_diagnostico: str
    diagnostico: str
    fecha: datetime
    formato_pdf: Optional[str] = None  # URL o ruta del archivo
    activo: bool = True

class ReporteCreate(ReporteBase):
    pass

class ReporteUpdate(BaseModel):
    diagnostico: Optional[str] = None
    formato_pdf: Optional[str] = None
    activo: Optional[bool] = None

class ReporteResponse(ReporteBase):
    id_reporte: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
