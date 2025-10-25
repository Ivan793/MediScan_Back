from fastapi import APIRouter, Query
from typing import List, Optional
from app.services.doctor_admin_service import DoctorAdminServicio
from app.schemas.doctor import DoctorRespuesta, DoctorActualizar

router = APIRouter(prefix="/admin/doctores", tags=["Doctores - Admin"])
servicio = DoctorAdminServicio()


@router.get("/", response_model=List[DoctorRespuesta])
async def listar_doctores(
    estado: Optional[str] = Query(None, description="Filtrar por estado: pendiente, aprobado, rechazado")
):
    """
    Lista doctores independientes registrados.
    - Permite filtrar por estado (pendiente, aprobado, rechazado).
    """
    return await servicio.listar_doctores(estado)


@router.put("/{id_doctor}/estado")
async def cambiar_estado_doctor(id_doctor: str, nuevo_estado: str):
    """
    Cambia el estado de un doctor a `aprobado` o `rechazado`.
    """
    return await servicio.cambiar_estado(id_doctor, nuevo_estado)


@router.put("/{id_doctor}", response_model=DoctorRespuesta)
async def actualizar_doctor(id_doctor: str, data: DoctorActualizar):
    """
    Actualiza información del doctor (solo accesible por admin).
    """
    return await servicio.actualizar_doctor(id_doctor, data)


@router.delete("/{id_doctor}")
async def eliminar_doctor(id_doctor: str):
    """
    Elimina un registro de doctor (solo para admin).
    """
    return await servicio.eliminar_doctor(id_doctor)
