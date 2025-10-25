from fastapi import APIRouter, Query
from typing import List, Optional
from app.services.empresa_admin_service import EmpresaAdminServicio
from app.schemas.empresa import EmpresaRespuesta, EmpresaCrear, EmpresaActualizar

router = APIRouter(prefix="/admin/empresas", tags=["Empresas - Admin"])
servicio = EmpresaAdminServicio()


@router.post("/", response_model=EmpresaRespuesta)
async def crear_empresa_admin(empresa: EmpresaCrear):
    """
    Permite al administrador registrar una nueva empresa directamente (ya aprobada).
    """
    return await servicio.crear_empresa(empresa)


@router.get("/", response_model=list[EmpresaRespuesta])
async def listar_empresas(estado: Optional[str] = Query(None, description="Filtrar por estado: pendiente, aprobada, rechazada")):
    return await servicio.listar_empresas(estado)

@router.get("/todas", response_model=List[EmpresaRespuesta])
async def listar_todas_las_empresas():
    """
    Retorna todas las empresas registradas, sin filtrar por estado.
    """
    return await servicio.listar_empresas()

@router.put("/{id_empresa}/estado")
async def cambiar_estado_empresa(id_empresa: str, nuevo_estado: str):
    return await servicio.cambiar_estado(id_empresa, nuevo_estado)


@router.put("/{id_empresa}", response_model=EmpresaRespuesta)
async def actualizar_empresa(id_empresa: str, data: EmpresaActualizar):
    return await servicio.actualizar_empresa(id_empresa, data)


@router.delete("/{id_empresa}")
async def eliminar_empresa(id_empresa: str):
    return await servicio.eliminar_empresa(id_empresa)
