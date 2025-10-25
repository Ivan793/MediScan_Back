from typing import List, Optional
from app.schemas.doctor import DoctorCreateWithUser, DoctorResponse
import uuid

# Simulamos almacenamiento local temporal
DOCTORS_DB: List[DoctorResponse] = []


class DoctorRepository:

    @staticmethod
    def create(doctor_data: DoctorCreateWithUser) -> DoctorResponse:
        new_doctor = DoctorResponse(
            id=str(uuid.uuid4()),
            nombre=doctor_data.nombre,
            especialidad=doctor_data.especialidad,
            usuario=doctor_data.usuario
        )
        DOCTORS_DB.append(new_doctor)
        return new_doctor

    @staticmethod
    def get_all() -> List[DoctorResponse]:
        return DOCTORS_DB

    @staticmethod
    def get_by_id(doctor_id: str) -> Optional[DoctorResponse]:
        for doctor in DOCTORS_DB:
            if doctor.id == doctor_id:
                return doctor
        return None

    @staticmethod
    def delete(doctor_id: str) -> bool:
        global DOCTORS_DB
        for d in DOCTORS_DB:
            if d.id == doctor_id:
                DOCTORS_DB.remove(d)
                return True
        return False
