from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


class UsuarioBase(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: str
    numero_documento: str
    correo: EmailStr
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None
    pais: Optional[str] = None
    fecha_nacimiento: Optional[datetime] = None
    genero: Optional[str] = None
    foto_perfil: Optional[str] = None
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nombres": "Juan Carlos",
                "apellidos": "Martínez López",
                "tipo_documento": "CC",
                "numero_documento": "1023456789",
                "correo": "juan.martinez@ejemplo.com",
                "telefono": "+57 3001234567",
                "direccion": "Calle 12 #34-56, Bogotá",
                "ciudad": "Bogotá",
                "pais": "Colombia",
                "fecha_nacimiento": "1990-05-10T00:00:00",
                "genero": "Masculino",
                "foto_perfil": "https://ejemplo.com/perfil.jpg",
                "fecha_registro": "2025-10-24T12:00:00"
            }
        }
    )


class UsuarioCrear(UsuarioBase):
    contraseña: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                **UsuarioBase.model_config["json_schema_extra"]["example"],
                "contraseña": "Usuario123#"
            }
        }
    )


class UsuarioActualizar(BaseModel):
    nombres: Optional[str] = None
    apellidos: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None
    pais: Optional[str] = None
    foto_perfil: Optional[str] = None
    contraseña: Optional[str] = None
    activo: Optional[bool] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "telefono": "+57 3112223344",
                "direccion": "Carrera 15 #45-10",
                "ciudad": "Medellín",
                "pais": "Colombia",
                "foto_perfil": "https://ejemplo.com/nueva_foto.jpg",
                "activo": True
            }
        }
    )


class UsuarioRespuesta(UsuarioBase):
    id: str
    activo: bool = True

    model_config = ConfigDict(from_attributes=True)
