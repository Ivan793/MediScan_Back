from datetime import datetime
from fastapi import HTTPException, status
from app.core.firebase import firebase_client as db
from app.schemas.empresa import EmpresaCrear, EmpresaActualizar, EmpresaRespuesta

COLECCION_EMPRESAS = "empresas"
COLECCION_USUARIOS = "usuarios"


class EmpresaAdminServicio:
    """
    Servicio para la gestión administrativa de empresas.
    Permite crear, listar, aprobar, rechazar, actualizar o eliminar registros.
    """

    async def crear_empresa(self, data: EmpresaCrear) -> EmpresaRespuesta:
        """
        Permite al admin crear una empresa y su usuario asociado directamente.
        Queda aprobada automáticamente.
        """
        empresa_dict = data.model_dump()
        usuario_dict = empresa_dict.pop("usuario")

        # Crear usuario
        usuario_ref = db.collection(COLECCION_USUARIOS).document()
        usuario_dict["id_usuario"] = usuario_ref.id
        usuario_dict["fecha_creacion"] = datetime.utcnow()
        usuario_ref.set(usuario_dict)

        # Crear empresa asociada
        empresa_ref = db.collection(COLECCION_EMPRESAS).document()
        empresa_dict["id_empresa"] = empresa_ref.id
        empresa_dict["id_usuario"] = usuario_ref.id
        empresa_dict["estado"] = "aprobada"
        empresa_dict["fecha_registro"] = datetime.utcnow()
        empresa_dict["fecha_verificacion"] = datetime.utcnow()

        empresa_ref.set(empresa_dict)

        return EmpresaRespuesta(**empresa_dict)

    async def listar_empresas(self, estado: str = None) -> list[EmpresaRespuesta]:
        coleccion = db.collection(COLECCION_EMPRESAS)
        if estado:
            query = coleccion.where("estado", "==", estado).stream()
        else:
            query = coleccion.stream()

        empresas = [doc.to_dict() for doc in query]
        return [EmpresaRespuesta(**empresa) for empresa in empresas]

    async def cambiar_estado(self, id_empresa: str, nuevo_estado: str) -> dict:
        empresa_ref = db.collection(COLECCION_EMPRESAS).document(id_empresa)
        empresa_doc = empresa_ref.get()

        if not empresa_doc.exists:
            raise HTTPException(status_code=404, detail="Empresa no encontrada")

        if nuevo_estado not in ["aprobada", "rechazada"]:
            raise HTTPException(status_code=400, detail="Estado no válido")

        empresa_ref.update({
            "estado": nuevo_estado,
            "fecha_verificacion": datetime.utcnow()
        })

        return {"mensaje": f"Empresa {nuevo_estado} correctamente"}

    async def actualizar_empresa(self, id_empresa: str, data: EmpresaActualizar) -> EmpresaRespuesta:
        empresa_ref = db.collection(COLECCION_EMPRESAS).document(id_empresa)
        empresa_doc = empresa_ref.get()

        if not empresa_doc.exists:
            raise HTTPException(status_code=404, detail="Empresa no encontrada")

        update_data = data.model_dump(exclude_unset=True)
        update_data["updated_at"] = datetime.utcnow()
        empresa_ref.update(update_data)

        empresa_actualizada = empresa_ref.get().to_dict()
        return EmpresaRespuesta(**empresa_actualizada)

    async def eliminar_empresa(self, id_empresa: str) -> dict:
        empresa_ref = db.collection(COLECCION_EMPRESAS).document(id_empresa)
        empresa_doc = empresa_ref.get()

        if not empresa_doc.exists:
            raise HTTPException(status_code=404, detail="Empresa no encontrada")

        empresa_ref.delete()
        return {"mensaje": "Empresa eliminada correctamente"}
