from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from app.schemas.persona import PersonaBase
from app.schemas.usuario import UsuarioCrear


class DoctorBase(PersonaBase):
    rethus: str
    numero_tarjeta_profesional: str
    especialidades: List[str]
    anio_graduacion: int
    archivo_tarjeta_profesional: Optional[str] = None
    archivo_titulo_grado: Optional[str] = None
    archivo_rethus: Optional[str] = None
    archivo_especialidad: Optional[str] = None
    id_usuario: Optional[str] = None
    id_empresa: Optional[str] = None  # ← Solo se llena si pertenece a una empresa

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nombres": "María Fernanda",
                "apellidos": "López Ramírez",
                "tipo_documento": "CC",
                "numero_documento": "1034567890",
                "telefono": "+573102223344",
                "direccion": "Carrera 12 #34-56",
                "ciudad": "Bogotá",
                "pais": "Colombia",
                "fecha_nacimiento": "1992-07-15T00:00:00",
                "genero": "Femenino",
                "rethus": "RTH-123456",
                "numero_tarjeta_profesional": "TP-987654",
                "especialidades": ["Neumología", "Medicina Interna"],
                "anio_graduacion": 2012,
                "archivo_tarjeta_profesional": "https://example.com/tarjeta_profesional.pdf",
                "archivo_titulo_grado": "https://example.com/titulo_grado.pdf",
                "archivo_rethus": "https://example.com/rethus.pdf",
                "archivo_especialidad": "https://example.com/especialidad.pdf",
                "id_usuario": "usr_123456",
                "id_empresa": None
            }
        }
    )


# 🔹 Crear doctor independiente (público)
class DoctorCrearIndependiente(DoctorBase):
    usuario: UsuarioCrear  # ← se crea el usuario en cascada

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nombres": "Camilo Andrés",
                "apellidos": "Pérez Suárez",
                "tipo_documento": "Cédula de Ciudadanía",
                "numero_documento": "1029384756",
                "telefono": "+573114445566",
                "direccion": "Calle 45 #22-10",
                "ciudad": "Bogotá",
                "pais": "Colombia",
                "fecha_nacimiento": "1985-03-20T00:00:00",
                "genero": "Masculino",
                "rethus": "RTH-543210",
                "numero_tarjeta_profesional": "TP-112233",
                "especialidades": ["Radiología", "Neumología"],
                "anio_graduacion": 2010,
                "archivo_tarjeta_profesional": "https://example.com/tarjeta_profesional.pdf",
                "archivo_titulo_grado": "https://example.com/titulo_grado.pdf",
                "archivo_rethus": "https://example.com/rethus.pdf",
                "archivo_especialidad": "https://example.com/especialidad.pdf",
                "usuario": {
                    "correo": "camilo.perez@mediscan.com",
                    "contrasenia": "Medico123#",
                    "id_rol": "doctor",
                    "foto_perfil_url": "https://example.com/foto_camilo.jpg"
                }
            }
        }
    )


# 🔹 Crear doctor asociado a una empresa
# 🔹 Crear doctor asociado a una empresa
class DoctorCrearEmpresa(DoctorBase):
    usuario: UsuarioCrear
    id_empresa: str  # ← obligatorio cuando lo crea una empresa

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "nombres": "Laura",
                "apellidos": "Gómez Torres",
                "tipo_documento": "Cédula de Ciudadanía",
                "numero_documento": "1234567890",
                "telefono": "+573005551122",
                "direccion": "Calle 10 #15-23",
                "ciudad": "Medellín",
                "pais": "Colombia",
                "fecha_nacimiento": "1990-04-12T00:00:00",
                "genero": "Femenino",
                "rethus": "RTH-765432",
                "numero_tarjeta_profesional": "TP-554433",
                "especialidades": ["Pediatría", "Cardiología"],
                "anio_graduacion": 2015,
                "archivo_tarjeta_profesional": "https://example.com/tarjeta_profesional.pdf",
                "archivo_titulo_grado": "https://example.com/titulo_grado.pdf",
                "archivo_rethus": "https://example.com/rethus.pdf",
                "archivo_especialidad": "https://example.com/especialidad.pdf",
                "id_empresa": "abc123empresa",
                "usuario": {
                    "correo": "laura.gomez@clinicavida.com",
                    "contrasenia": "DoctorEmpresa123#",
                    "id_rol": "doctor",
                    "foto_perfil_url": "https://example.com/laura.jpg"
                }
            }
        }
    )


# 🔹 Actualización del doctor
class DoctorActualizar(BaseModel):
    especialidades: Optional[List[str]] = None
    anio_graduacion: Optional[int] = None
    archivo_tarjeta_profesional: Optional[str] = None
    archivo_titulo_grado: Optional[str] = None
    archivo_rethus: Optional[str] = None
    archivo_especialidad: Optional[str] = None
    activo: Optional[bool] = None
    id_empresa: Optional[str] = None

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


# 🔹 Respuesta al consultar un doctor
class DoctorRespuesta(DoctorBase):
    id_doctor: str
    id_usuario: str
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id_doctor": "doc_987654",
                "id_usuario": "usr_123456",
                "nombres": "Camilo Andrés",
                "apellidos": "Pérez Suárez",
                "tipo_documento": "CC",
                "numero_documento": "1029384756",
                "telefono": "+573114445566",
                "direccion": "Calle 45 #22-10",
                "ciudad": "Bogotá",
                "pais": "Colombia",
                "fecha_nacimiento": "1985-03-20T00:00:00",
                "genero": "Masculino",
                "rethus": "RTH-543210",
                "numero_tarjeta_profesional": "TP-112233",
                "especialidades": ["Radiología", "Neumología"],
                "anio_graduacion": 2010,
                "archivo_tarjeta_profesional": "https://example.com/tarjeta_profesional.pdf",
                "archivo_titulo_grado": "https://example.com/titulo_grado.pdf",
                "archivo_rethus": "https://example.com/rethus.pdf",
                "archivo_especialidad": "https://example.com/especialidad.pdf",
                "id_empresa": "abc123empresa",
                "creado_en": "2025-10-24T12:00:00",
                "actualizado_en": "2025-10-25T12:00:00"
            }
        }
    )
