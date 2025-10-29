from fastapi import APIRouter, Depends, Request, HTTPException
from firebase_admin import auth as firebase_auth
from app.services.auth_service import AuthServicio

router = APIRouter(prefix="/auth", tags=["Autenticación"])
servicio = AuthServicio()


from pydantic import BaseModel
from firebase_admin import auth

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    try:
        user = auth.get_user_by_email(data.email)
        custom_token = auth.create_custom_token(user.uid)
        return {
            "message": "Login correcto",
            "uid": user.uid,
            "email": user.email,
            "custom_token": custom_token.decode("utf-8")
        }
    except auth.UserNotFoundError:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Error en login: {e}")


@router.get("/me")
def get_me(current_user=Depends(servicio.get_current_user)):
    return {
        "uid": current_user["uid"],
        "email": current_user.get("email"),
        "role": current_user.get("role")
    }


@router.post("/assign-role")
@servicio.role_required(["superadmin"])
async def assign_role_route(request: Request, uid: str, role: str, current_user=None):
    return servicio.assign_role(uid, role)
