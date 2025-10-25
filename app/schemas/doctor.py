from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime

from app.schemas.usuario import UserCreate  # Importamos el schema base del usuario


class DoctorBase(BaseModel):
    rethus: str
    numero_tarjeta_profesional: str
    especialidades: List[str]
    anio_graduacion: int
    archivo_tarjeta_profesional: Optional[str] = None
    archivo_titulo_grado: Optional[str] = None
    archivo_rethus: Optional[str] = None
    archivo_especialidad: Optional[str] = None
    activo: bool = True

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "rethus": "RTH-123456",
                "numero_tarjeta_profesional": "TP-987654",
                "especialidades": ["Neumología", "Medicina Interna"],
                "anio_graduacion": 2012,
                "archivo_tarjeta_profesional": "https://example.com/tarjeta_profesional.pdf",
                "archivo_titulo_grado": "https://example.com/titulo_grado.pdf",
                "archivo_rethus": "https://example.com/rethus.pdf",
                "archivo_especialidad": "https://example.com/especialidad.pdf",
                "activo": True
            }
        }
    )


# Crear doctor junto con su usuario (en cascada)
class DoctorCreateWithUser(DoctorBase):
    usuario: UserCreate

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "usuario": {
                    "nombres": "Camilo Andrés",
                    "apellidos": "Pérez Suárez",
                    "tipo_documento": "CC",
                    "numero_documento": "1029384756",
                    "email": "camilo.perez@mediscan.com",
                    "telefono": "+573114445566",
                    "direccion": "Calle 45 #22-10",
                    "ciudad": "Bogotá",
                    "pais": "Colombia",
                    "fecha_nacimiento": "1985-03-20T00:00:00",
                    "genero": "Masculino",
                    "foto_perfil": "https://example.com/foto_camilo.jpg",
                    "password": "Medico123#"
                },
                "rethus": "RTH-543210",
                "numero_tarjeta_profesional": "TP-112233",
                "especialidades": ["Radiología", "Neumología"],
                "anio_graduacion": 2010,
                "archivo_tarjeta_profesional": "https://example.com/tarjeta_profesional.pdf",
                "archivo_titulo_grado": "https://example.com/titulo_grado.pdf",
                "archivo_rethus": "https://example.com/rethus.pdf",
                "archivo_especialidad": "https://example.com/especialidad.pdf",
                "activo": True
            }
        }
    )


class DoctorUpdate(BaseModel):
    especialidades: Optional[List[str]] = None
    anio_graduacion: Optional[int] = None
    archivo_tarjeta_profesional: Optional[str] = None
    archivo_titulo_grado: Optional[str] = None
    archivo_rethus: Optional[str] = None
    archivo_especialidad: Optional[str] = None
    activo: Optional[bool] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "especialidades": ["Medicina Interna", "Neumología"],
                "anio_graduacion": 2011,
                "archivo_rethus": "https://example.com/nuevo_rethus.pdf",
                "activo": True
            }
        }
    )


class DoctorResponse(DoctorBase):
    id: str
    id_usuario: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
