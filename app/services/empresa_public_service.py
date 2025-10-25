from datetime import datetime
from fastapi import HTTPException, status
from app.core.firebase import firebase_client as db
from google.cloud import firestore
from app.schemas.empresa import EmpresaCrear, EmpresaRespuesta

COLECCION_EMPRESAS = "empresas"
COLECCION_USUARIOS = "usuarios"


class EmpresaPublicaServicio:
    """
    Servicio para el registro y consulta pública de empresas.
    """

    async def registrar_empresa(self, data: EmpresaCrear) -> EmpresaRespuesta:
        """
        Crea una empresa y su usuario asociado.
        La empresa queda con estado 'pendiente' hasta que un administrador la apruebe.
        """
        empresa_dict = data.model_dump()
        usuario_dict = empresa_dict.pop("usuario")  # 👈 separar los datos del usuario

        # Crear el usuario en Firestore
        usuario_ref = db.collection(COLECCION_USUARIOS).document()
        usuario_dict["id_usuario"] = usuario_ref.id
        usuario_dict["fecha_creacion"] = datetime.utcnow()
        usuario_ref.set(usuario_dict)

        # Crear la empresa asociando el id_usuario
        empresa_ref = db.collection(COLECCION_EMPRESAS).document()
        empresa_dict["id_empresa"] = empresa_ref.id
        empresa_dict["id_usuario"] = usuario_ref.id  # 👈 relación en cascada
        empresa_dict["estado"] = "pendiente"
        empresa_dict["fecha_registro"] = datetime.utcnow()

        empresa_ref.set(empresa_dict)

        # Retornar la empresa creada
        return EmpresaRespuesta(**empresa_dict)

    async def consultar_estado(self, nit: str) -> dict:
        """
        Permite al público verificar si su empresa fue aprobada o rechazada.
        """
        query = db.collection(COLECCION_EMPRESAS).where("nit", "==", nit).limit(1).stream()
        docs = list(query)

        if not docs:
            raise HTTPException(status_code=404, detail="Empresa no encontrada")

        empresa = docs[0].to_dict()
        return {
            "razon_social": empresa.get("razon_social"),
            "estado": empresa.get("estado"),
            "fecha_verificacion": empresa.get("fecha_verificacion"),
        }
