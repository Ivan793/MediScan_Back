from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from app.core.depedencies import get_current_user
from app.services.doctor_independiente_service import DoctorIndependienteServicio
from app.schemas.doctor import DoctorRespuesta, DoctorCrearIndependiente, DoctorActualizar

router = APIRouter(prefix="/doctores/independientes", tags=["Doctores - Independientes"])
servicio = DoctorIndependienteServicio()


@router.post("/", response_model=DoctorRespuesta, status_code=201)
async def registrar_doctor_independiente(doctor: DoctorCrearIndependiente):
    """
    Permite a un **doctor independiente** registrarse en la plataforma.
    - El registro es **público**.
    - Queda inicialmente en estado **pendiente** hasta que un administrador lo apruebe.
    """
    return await servicio.crear_doctor_independiente(doctor)


@router.get("/", response_model=List[DoctorRespuesta])
async def listar_doctores_independientes(
    estado: Optional[str] = Query(None, description="Filtrar por estado: pendiente, aprobado, rechazado")
):
    """
    Lista todos los doctores independientes registrados.
    - Puede filtrarse por `estado` (pendiente, aprobado, rechazado).
    """
    return await servicio.listar_doctores(estado)

@router.get("/estado", summary="Consulta autenticada del estado del doctor")
async def obtener_estado_doctor(current_user: dict = Depends(get_current_user)):
    """
    Permite que un doctor autenticado consulte su propio estado.
    """
    id_usuario = current_user["id_usuario"]
    return await servicio.obtener_estado_por_id_usuario(id_usuario)


@router.get("/estado-publico", summary="Consulta pública del estado del doctor")
async def obtener_estado_por_tarjeta(
    numero_tarjeta_profesional: str = Query(..., description="Número de tarjeta profesional del doctor")
):
    """
    Permite consultar públicamente el estado de un doctor por su número de tarjeta profesional.
    """
    return await servicio.obtener_estado_por_tarjeta(numero_tarjeta_profesional)

@router.put("/{id_doctor}", response_model=DoctorRespuesta)
async def actualizar_doctor_independiente(id_doctor: str, data: DoctorActualizar):
    """
    Permite actualizar la información de un **doctor independiente**.
    - Puede ser usado tanto por el propio doctor como por un administrador.
    """
    return await servicio.actualizar_doctor(id_doctor, data)


@router.delete("/{id_doctor}")
async def eliminar_doctor_independiente(id_doctor: str):
    """
    Elimina el registro de un **doctor independiente**.
    - Solo debería ser ejecutado por un administrador.
    """
    return await servicio.eliminar_doctor(id_doctor)
