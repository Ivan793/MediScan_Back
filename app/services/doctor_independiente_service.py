from datetime import datetime
from fastapi import HTTPException, status
from app.core.firebase import firebase_client as db
from app.schemas.doctor import DoctorCrearIndependiente, DoctorActualizar, DoctorRespuesta

COLECCION_DOCTORES = "doctores"
COLECCION_USUARIOS = "usuarios"


class DoctorIndependienteServicio:
    """
    Servicio para la gestión de doctores independientes.
    Permite registrar doctores públicos (pendientes de aprobación),
    listar, actualizar y eliminar doctores independientes.
    """

    async def crear_doctor_independiente(self, data: DoctorCrearIndependiente) -> DoctorRespuesta:
        """
        Permite registrar un doctor independiente con creación de usuario en cascada.
        El estado inicial es 'pendiente' hasta que el admin lo apruebe.
        """
        doctor_dict = data.model_dump()
        usuario_dict = doctor_dict.pop("usuario")

        # Crear usuario asociado
        usuario_ref = db.collection(COLECCION_USUARIOS).document()
        usuario_dict["id_usuario"] = usuario_ref.id
        usuario_dict["fecha_creacion"] = datetime.utcnow()
        usuario_dict["rol"] = "doctor_independiente"
        usuario_ref.set(usuario_dict)

        # Crear doctor asociado
        doctor_ref = db.collection(COLECCION_DOCTORES).document()
        doctor_dict["id_doctor"] = doctor_ref.id
        doctor_dict["id_usuario"] = usuario_ref.id
        doctor_dict["estado"] = "pendiente"
        doctor_dict["creado_en"] = datetime.utcnow()
        doctor_dict["actualizado_en"] = datetime.utcnow()

        doctor_ref.set(doctor_dict)

        return DoctorRespuesta(**doctor_dict)

    async def listar_doctores(self, estado: str = None) -> list[DoctorRespuesta]:
        """
        Lista doctores independientes, opcionalmente filtrando por estado.
        """
        coleccion = db.collection(COLECCION_DOCTORES)
        if estado:
            query = coleccion.where("estado", "==", estado).stream()
        else:
            query = coleccion.stream()

        doctores = [doc.to_dict() for doc in query]
        return [DoctorRespuesta(**doctor) for doctor in doctores]
    
    
    
    async def actualizar_doctor(self, id_doctor: str, data: DoctorActualizar) -> DoctorRespuesta:
        """
        Actualiza los datos de un doctor independiente.
        """
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
        """
        Elimina un registro de doctor independiente.
        """
        doctor_ref = db.collection(COLECCION_DOCTORES).document(id_doctor)
        doctor_doc = doctor_ref.get()

        if not doctor_doc.exists:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")

        doctor_ref.delete()
        return {"mensaje": "Doctor eliminado correctamente"}
    
    async def obtener_estado_por_id_usuario(self, id_usuario: str) -> dict:
        """
        Permite que un doctor autenticado consulte su propio estado.
        """
        doctores_ref = db.collection(COLECCION_DOCTORES)
        query = doctores_ref.where("id_usuario", "==", id_usuario).stream()
        doctor = next(query, None)

        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")

        return {"estado": doctor.to_dict()["estado"]}
    

    async def obtener_estado_por_tarjeta(self, numero_tarjeta_profesional: str) -> dict:
        """
        Permite consultar el estado del doctor de forma pública usando su número de tarjeta profesional.
        """
        doctores_ref = db.collection(COLECCION_DOCTORES)
        query = doctores_ref.where("numero_tarjeta_profesional", "==", numero_tarjeta_profesional).stream()
        doctor = next(query, None)

        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor no encontrado")

        return {"estado del doctor": doctor.to_dict()["estado"]}
