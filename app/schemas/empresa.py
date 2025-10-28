from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional, List, Literal
from datetime import datetime
from app.schemas.usuario import UsuarioCrear


class EmpresaBase(BaseModel):
    nit: str
    razon_social: str
    licencia_funcionamiento: str
    archivo_licencia_funcionamiento: Optional[str] = None
    direccion: str
    ciudad: str
    departamento: str
    pais: str
    telefono: str
    correo_contacto: Optional[EmailStr] = None
    regimen: Optional[str] = None
    ips: Optional[str] = None
    servicios: Optional[List[str]] = Field(default_factory=list)
    sedes: Optional[List[str]] = Field(default_factory=list)
    estado: Literal["pendiente", "aprobada", "rechazada"] = Field(default="pendiente")
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)
    fecha_verificacion: Optional[datetime] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nit": "900123456-1",
                "razon_social": "Clínica Vida Plena S.A.",
                "licencia_funcionamiento": "LF-2025-001",
                "archivo_licencia_funcionamiento": "licencia_vida_plena.pdf",
                "direccion": "Calle 12 #45-67",
                "ciudad": "Medellín",
                "departamento": "Antioquia",
                "pais": "Colombia",
                "telefono": "+5741234567",
                "correo_contacto": "contacto@vidaplena.com",
                "regimen": "Contributivo",
                "ips": "IPS Vida Plena",
                "servicios": ["Medicina general", "Odontología"],
                "sedes": ["Sede Norte", "Sede Sur"],
                "estado": "pendiente",
                "fecha_registro": "2025-10-24T12:00:00"
            }
        }
    )


class EmpresaCrear(EmpresaBase):
    usuario: UsuarioCrear

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "usuario": {
                    "correo": "contacto@vidaplena.com",
                    "contrasenia": "Usuario123#",
                    "id_rol": "empresa",
                    "foto_perfil_url": "https://ejemplo.com/foto_empresa.jpg"
                },
                "nit": "900123456-1",
                "razon_social": "Clínica Vida Plena S.A.",
                "licencia_funcionamiento": "LF-2025-001",
                "archivo_licencia_funcionamiento": "licencia_vida_plena.pdf",
                "direccion": "Calle 12 #45-67",
                "ciudad": "Medellín",
                "departamento": "Antioquia",
                "pais": "Colombia",
                "telefono": "+5741234567",
                "correo_contacto": "contacto@vidaplena.com",
                "regimen": "Contributivo",
                "ips": "IPS Vida Plena",
                "servicios": ["Medicina general", "Odontología"],
                "sedes": ["Sede Norte", "Sede Sur"]
            }
        }
    )


class EmpresaActualizar(BaseModel):
    razon_social: Optional[str] = None
    licencia_funcionamiento: Optional[str] = None
    archivo_licencia_funcionamiento: Optional[str] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None
    departamento: Optional[str] = None
    pais: Optional[str] = None
    telefono: Optional[str] = None
    correo_contacto: Optional[EmailStr] = None
    regimen: Optional[str] = None
    ips: Optional[str] = None
    servicios: Optional[List[str]] = None
    sedes: Optional[List[str]] = None
    estado: Optional[Literal["pendiente", "aprobada", "rechazada"]] = None
    fecha_verificacion: Optional[datetime] = None

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "razon_social": "Clínica Vida Plena Renovada S.A.",
                "direccion": "Carrera 25 #10-55",
                "telefono": "+5747654321",
                "correo_contacto": "nuevocontacto@vidaplena.com",
                "regimen": "Subsidiado",
                "ips": "IPS Vida Plena Renovada",
                "servicios": ["Medicina general", "Fisioterapia"],
                "sedes": ["Sede Central", "Sede Sur"],
                "estado": "aprobada",
                "fecha_verificacion": "2025-10-28T09:00:00"
            }
        }
    )


class EmpresaRespuesta(EmpresaBase):
    id_empresa: str
    id_usuario: Optional[str] = None
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id_empresa": "emp_001",
                "id_usuario": "usr_001",
                "nit": "900123456-1",
                "razon_social": "Clínica Vida Plena S.A.",
                "licencia_funcionamiento": "LF-2025-001",
                "direccion": "Calle 12 #45-67",
                "ciudad": "Medellín",
                "departamento": "Antioquia",
                "pais": "Colombia",
                "telefono": "+5741234567",
                "correo_contacto": "contacto@vidaplena.com",
                "regimen": "Contributivo",
                "ips": "IPS Vida Plena",
                "servicios": ["Medicina general", "Odontología"],
                "sedes": ["Sede Norte", "Sede Sur"],
                "estado": "aprobada",
                "fecha_registro": "2025-10-24T12:00:00",
                "fecha_verificacion": "2025-10-28T08:00:00",
                "creado_en": "2025-10-24T12:00:00",
                "actualizado_en": "2025-10-28T09:00:00"
            }
        }
    )
