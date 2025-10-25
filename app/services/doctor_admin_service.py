from datetime import datetime
from fastapi import HTTPException
from app.core.firebase import firebase_client as db
from app.schemas.doctor import DoctorRespuesta, DoctorActualizar

COLECCION_DOCTORES = "doctores"


class DoctorAdminServicio:
    """
    Servicio para la gestión administrativa de doctores independientes.
    Permite listar, aprobar, rechazar, actualizar o eliminar doctores.
    """

    async def listar_doctores(self, estado: str = None) -> list[DoctorRespuesta]:
        coleccion = db.collection(COLECCION_DOCTORES)
        if estado:
            query = coleccion.where("estado", "==", estado).stream()
        else:
            query = coleccion.stream()

        doctores = [doc.to_dict() for doc in query]
        return [DoctorRespuesta(**doctor) for doctor in doctores]

    async def cambiar_estado(self, id_doctor: str, nuevo_estado: str) -> dict:
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
        doctor_ref = db.collection(COLECCION_DOCTORES).document(id_doctor)
        doctor_doc = doctor_ref.get()

        if not doctor_doc.exists:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")

        update_data = data.model_dump(exclude_unset=True)
        update_data["actualizado_en"] = datetime.utcnow()
        doctor_ref.update(update_data)

        doctor_actualizado = doctor_ref.get().to_dict()
        return DoctorRespuesta(**doctor_actualizado)

    async def eliminar_doctor(self, id_doctor: str) -> dict:
        doctor_ref = db.collection(COLECCION_DOCTORES).document(id_doctor)
        doctor_doc = doctor_ref.get()

        if not doctor_doc.exists:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")

        doctor_ref.delete()
        return {"mensaje": "Doctor eliminado correctamente"}
