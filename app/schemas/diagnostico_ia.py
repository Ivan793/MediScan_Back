# app/schemas/diagnostico_ia.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class DiagnosticoIABase(BaseModel):
    id_radiografia: str
    resultado: str
    confianza: float = Field(..., ge=0, le=1)

class DiagnosticoIACreate(DiagnosticoIABase):
    pass

class DiagnosticoIAUpdate(BaseModel):
    resultado: Optional[str] = None
    confianza: Optional[float] = None

class DiagnosticoIAResponse(DiagnosticoIABase):
    id_diagnostico: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
