from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


class UsuarioBase(BaseModel):
    correo: EmailStr
    contrasenia_hash: str
    activo: bool = True
    foto_perfil_url: Optional[str] = None
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)
    fecha_ultima_actualizacion: datetime = Field(default_factory=datetime.utcnow)
    id_rol: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "correo": "juan.martinez@ejemplo.com",
                "contrasenia_hash": "hash_de_contraseña_123",
                "activo": True,
                "foto_perfil_url": "https://ejemplo.com/perfil.jpg",
                "fecha_creacion": "2025-10-24T12:00:00",
                "fecha_ultima_actualizacion": "2025-10-24T12:00:00",
                "id_rol": "empresa"
            }
        }
    )


class UsuarioCrear(BaseModel):
    correo: EmailStr
    contrasenia: str
    id_rol: str
    foto_perfil_url: Optional[str] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "correo": "maria.lopez@ejemplo.com",
                "contrasenia": "Usuario123#",
                "id_rol": "paciente",
                "foto_perfil_url": "https://ejemplo.com/foto.jpg"
            }
        }
    )


class UsuarioActualizar(BaseModel):
    correo: Optional[EmailStr] = None
    contrasenia: Optional[str] = None
    foto_perfil_url: Optional[str] = None
    activo: Optional[bool] = None
    id_rol: Optional[str] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "correo": "nuevo.correo@ejemplo.com",
                "contrasenia": "NuevaContraseña123!",
                "foto_perfil_url": "https://ejemplo.com/nueva_foto.jpg",
                "activo": False,
                "id_rol": "doctor"
            }
        }
    )


class UsuarioRespuesta(UsuarioBase):
    id: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "usr_123456",
                "correo": "juan.martinez@ejemplo.com",
                "contrasenia_hash": "hash_de_contraseña_123",
                "activo": True,
                "foto_perfil_url": "https://ejemplo.com/perfil.jpg",
                "fecha_creacion": "2025-10-24T12:00:00",
                "fecha_ultima_actualizacion": "2025-10-24T12:00:00",
                "id_rol": "empresa"
            }
        }
    )
