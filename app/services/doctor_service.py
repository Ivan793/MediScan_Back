from typing import List, Optional
from app.schemas.doctor import DoctorCreateWithUser, DoctorResponse
from app.repositories.doctor_repository import DoctorRepository
from app.services.usuario_service import UserService


class DoctorService:
    @staticmethod
    def create_doctor(doctor_data: DoctorCreateWithUser) -> DoctorResponse:
        # 🔹 Validar si el correo del usuario ya existe
        existing_users = UserService.get_all_users()
        for u in existing_users:
            if u.email == doctor_data.usuario.email:
                raise ValueError("Ya existe un usuario con ese correo.")

        # 🔹 Crear doctor (crea también su usuario en cascada)
        doctor = DoctorRepository.create(doctor_data)
        return doctor

    @staticmethod
    def get_all_doctors() -> List[DoctorResponse]:
        return DoctorRepository.get_all()

    @staticmethod
    def get_doctor_by_id(doctor_id: str) -> Optional[DoctorResponse]:
        doctor = DoctorRepository.get_by_id(doctor_id)
        if not doctor:
            raise ValueError("Doctor no encontrado.")
        return doctor

    @staticmethod
    def delete_doctor(doctor_id: str) -> bool:
        deleted = DoctorRepository.delete(doctor_id)
        if not deleted:
            raise ValueError("No se pudo eliminar el doctor, ID no encontrado.")
        return True
