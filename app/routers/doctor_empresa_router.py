from fastapi import APIRouter, Query
from typing import List, Optional
from app.services.doctor_empresa_service import DoctorEmpresaServicio
from app.schemas.doctor import DoctorRespuesta, DoctorCrearEmpresa, DoctorActualizar

router = APIRouter(prefix="/doctores/empresa", tags=["Doctores - Empresa"])
servicio = DoctorEmpresaServicio()


@router.post("/", response_model=DoctorRespuesta)
async def crear_doctor_empresa(doctor: DoctorCrearEmpresa):
    """
    Permite a una empresa registrar un nuevo doctor.
    """
    return await servicio.crear_doctor_empresa(doctor)


@router.get("/{id_empresa}", response_model=List[DoctorRespuesta])
async def listar_doctores_empresa(id_empresa: str):
    """
    Lista todos los doctores asociados a una empresa específica.
    """
    return await servicio.listar_doctores_por_empresa(id_empresa)


@router.put("/{id_doctor}/estado")
async def cambiar_estado_doctor(id_doctor: str, nuevo_estado: str):
    """
    Permite al admin cambiar el estado de un doctor (aprobado/rechazado).
    """
    return await servicio.cambiar_estado(id_doctor, nuevo_estado)


@router.put("/{id_doctor}", response_model=DoctorRespuesta)
async def actualizar_doctor_empresa(id_doctor: str, data: DoctorActualizar):
    """
    Permite actualizar la información del doctor.
    """
    return await servicio.actualizar_doctor(id_doctor, data)
