from datetime import datetime
from fastapi import HTTPException, status
from app.core.firebase import firebase_client as db
from app.schemas.doctor import DoctorCrearEmpresa, DoctorActualizar, DoctorRespuesta

COLECCION_DOCTORES = "doctores"
COLECCION_USUARIOS = "usuarios"


class DoctorEmpresaServicio:
    """
    Servicio para la gestión de doctores asociados a empresas.
    """

    async def crear_doctor_empresa(self, data: DoctorCrearEmpresa) -> DoctorRespuesta:
        """
        Permite que una empresa cree un nuevo doctor (estado inicial: pendiente).
        """
        doctor_dict = data.model_dump()
        usuario_dict = doctor_dict.pop("usuario")
        id_empresa = doctor_dict.get("id_empresa")

        if not id_empresa:
            raise HTTPException(status_code=400, detail="El ID de la empresa es obligatorio")

        # Crear usuario
        usuario_ref = db.collection(COLECCION_USUARIOS).document()
        usuario_dict["id_usuario"] = usuario_ref.id
        usuario_dict["fecha_creacion"] = datetime.utcnow()
        usuario_ref.set(usuario_dict)

        # Crear doctor asociado a la empresa
        doctor_ref = db.collection(COLECCION_DOCTORES).document()
        doctor_dict["id_doctor"] = doctor_ref.id
        doctor_dict["id_usuario"] = usuario_ref.id
        doctor_dict["estado"] = "pendiente"
        doctor_dict["fecha_registro"] = datetime.utcnow()
        doctor_dict["creado_en"] = datetime.utcnow()
        doctor_ref.set(doctor_dict)

        return DoctorRespuesta(**doctor_dict)

    async def listar_doctores_por_empresa(self, id_empresa: str) -> list[DoctorRespuesta]:
        """
        Lista todos los doctores asociados a una empresa específica.
        """
        doctores_ref = db.collection(COLECCION_DOCTORES)
        query = doctores_ref.where("id_empresa", "==", id_empresa).stream()
        doctores = [doc.to_dict() for doc in query]
        return [DoctorRespuesta(**d) for d in doctores]

    async def cambiar_estado(self, id_doctor: str, nuevo_estado: str) -> dict:
        """
        Permite al administrador aprobar o rechazar doctores de empresa.
        """
        doctor_ref = db.collection(COLECCION_DOCTORES).document(id_doctor)
        doctor_doc = doctor_ref.get()

        if not doctor_doc.exists:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")

        if nuevo_estado not in ["aprobado", "rechazado"]:
            raise HTTPException(status_code=400, detail="Estado no válido")

        doctor_ref.update({
            "estado": nuevo_estado,
            "fecha_verificacion": datetime.utcnow()
        })

        return {"mensaje": f"Doctor {nuevo_estado} correctamente"}

    async def actualizar_doctor(self, id_doctor: str, data: DoctorActualizar) -> DoctorRespuesta:
        """
        Permite actualizar la información de un doctor asociado a una empresa.
        """
        doctor_ref = db.collection(COLECCION_DOCTORES).document(id_doctor)
        doctor_doc = doctor_ref.get()

        if not doctor_doc.exists:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")

        update_data = data.model_dump(exclude_unset=True)
        update_data["actualizado_en"] = datetime.utcnow()
        doctor_ref.update(update_data)

        actualizado = doctor_ref.get().to_dict()
        return DoctorRespuesta(**actualizado)
