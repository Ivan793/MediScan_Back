from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict
from app.schemas.enums.tipo_documento import TipoDocumentoEnum
from app.schemas.enums.genero import GeneroEnum  

class PersonaBase(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: TipoDocumentoEnum
    numero_documento: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None
    pais: Optional[str] = None
    fecha_nacimiento: datetime
    genero: GeneroEnum

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nombres": "María Fernanda",
                "apellidos": "López Ramírez",
                "tipo_documento": "Cédula de Ciudadanía",
                "numero_documento": "1034567890",
                "telefono": "+573102223344",
                "direccion": "Carrera 12 #34-56",
                "ciudad": "Bogotá",
                "pais": "Colombia",
                "fecha_nacimiento": "1992-07-15T00:00:00",
                "genero": "Femenino"
            }
        }
    )
