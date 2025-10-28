# app/schemas/diagnostico_radiologico.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class DiagnosticoRadiologicoBase(BaseModel):
    id_radiografia: str
    id_doctor: str
    fecha_diagnostico: datetime = Field(default_factory=datetime.utcnow)
    hallazgos: Optional[str] = None
    impresion_diagnostica: Optional[str] = None
    recomendaciones: Optional[str] = None
    porcentaje_confianza: Optional[float] = None

class DiagnosticoRadiologicoCreate(DiagnosticoRadiologicoBase):
    pass

class DiagnosticoRadiologicoUpdate(BaseModel):
    hallazgos: Optional[str] = None
    impresion_diagnostica: Optional[str] = None
    recomendaciones: Optional[str] = None
    nivel_confianza: Optional[float] = None
    firmado_por_medico: Optional[bool] = None
    activo: Optional[bool] = None

class DiagnosticoRadiologicoResponse(DiagnosticoRadiologicoBase):
    id_diagnostico: str
    creado_en: datetime = Field(default_factory=datetime.utcnow)
    actualizado_en: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
