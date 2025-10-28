from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Optional, Literal

class RadiografiaToraxicaIABase(BaseModel):
    fecha_estudio: datetime = Field(default_factory=datetime.utcnow)
    tipo_proyeccion: Literal["PA", "AP", "Lateral", "AP-Lateral", "Otras"]
    motivo_examen: Optional[str] = None
    url_imagen: HttpUrl
    id_paciente: str
    id_doctor: str
    observaciones: Optional[str] = None
    fecha_informe: Optional[datetime] = None
    activo: bool = True


class RadiografiaToraxicaIACreate(RadiografiaToracicaBase):
    pass

class RadiografiaToraxicaIAUpdate(BaseModel):
    motivo_examen: Optional[str] = None
    observaciones_tecnicas: Optional[str] = None
    activo: Optional[bool] = None

class RadiografiaToraxicaIAResponse(RadiografiaToracicaBase):
    id_radiografia: str
    creado_en: datetime = Field(default_factory=datetime.utcnow)
    actualizado_en: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
