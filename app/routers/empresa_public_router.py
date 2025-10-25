from fastapi import APIRouter, HTTPException
from app.services.empresa_public_service import EmpresaPublicaServicio
from app.schemas.empresa import EmpresaRespuesta, EmpresaCrear

router = APIRouter(prefix="/empresas", tags=["Empresas - Público"])
servicio = EmpresaPublicaServicio()


@router.post("/", response_model=EmpresaRespuesta)
async def registrar_empresa_publica(empresa: EmpresaCrear):
    """
    Permite el registro público de una empresa.
    Quedará en estado 'pendiente' hasta que un administrador la verifique.
    """
    nueva_empresa = await servicio.registrar_empresa(empresa)
    return nueva_empresa


@router.get("/estado/{nit}")
async def consultar_estado_empresa(nit: str):
    """
    Permite al público consultar el estado de verificación de su empresa mediante el NIT.
    """
    resultado = await servicio.consultar_estado(nit)
    return resultado
