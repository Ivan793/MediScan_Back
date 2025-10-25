# app/services/auth_service.py
from app.core.depedencies import crear_token
from app.core.config import settings

# Usuario admin fijo
ADMIN_USER = {
    "email": "admin@mediscan.com",
    "password": "Admin123!",
    "rol": "admin"
}

class AuthService:
    @staticmethod
    def authenticate_user(email: str, password: str):
        """Valida credenciales y crea JWT si son correctas."""
        if email == ADMIN_USER["email"] and password == ADMIN_USER["password"]:
            token = crear_token(
                data={"sub": ADMIN_USER["email"], "rol": ADMIN_USER["rol"]},
                expires_delta=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
            return token
        return None
