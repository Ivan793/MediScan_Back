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
    correo_contacto: EmailStr
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
                "contraseña": "Usuario123#",
                "regimen": "Contributivo",
                "ips": "IPS Vida Plena",
                "servicios": ["Medicina general", "Odontología"],
                "sedes": ["Sede Norte", "Sede Sur"],
                "estado": "pendiente"
            }
        }
    )


class EmpresaCrear(EmpresaBase):
    usuario: UsuarioCrear

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "usuario": {
                    "tipo_documento": "NIT",
                    "numero_documento": "900123456-1",
                    "nombres": "Clínica Vida Plena",
                    "apellidos": "",
                    "correo": "contacto@vidaplena.com",
                    "contraseña": "Usuario123#",
                    "telefono": "+5741234567",
                    "direccion": "Calle 12 #45-67",
                    "ciudad": "Medellín",
                    "pais": "Colombia",
                    "fecha_nacimiento": "2000-01-01",
                    "genero": "Otro",
                    "rol": "empresa"
                },
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
    contraseña:Optional[str] = None
    regimen: Optional[str] = None
    ips: Optional[str] = None
    servicios: Optional[List[str]] = None
    sedes: Optional[List[str]] = None
    estado: Optional[str] = None
    fecha_verificacion: Optional[datetime] = None


class EmpresaRespuesta(EmpresaBase):
    id_empresa: str
    id_usuario: Optional[str] 
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
