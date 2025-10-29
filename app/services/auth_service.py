from fastapi import HTTPException, status, Header, Request
from firebase_admin import auth as firebase_auth, exceptions
from functools import wraps


class AuthServicio:

    @staticmethod
    def get_current_user(authorization: str = Header(None)):
        if not authorization:
            raise HTTPException(status_code=401, detail="Token no proporcionado")

        try:
            token = authorization.split(" ")[1]
            decoded_token = firebase_auth.verify_id_token(token)
            return decoded_token
        except exceptions.FirebaseError:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")

    @staticmethod
    def role_required(allowed_roles: list[str]):
        def decorator(func):
            @wraps(func)
            async def wrapper(request: Request, *args, **kwargs):
                auth_header = request.headers.get("Authorization")
                if not auth_header:
                    raise HTTPException(status_code=401, detail="Token no proporcionado")

                try:
                    token = auth_header.split(" ")[1]
                    decoded_token = firebase_auth.verify_id_token(token)
                    user_role = decoded_token.get("role")

                    if user_role not in allowed_roles:
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"No tienes permisos. Se requiere uno de estos roles: {allowed_roles}"
                        )

                    kwargs["current_user"] = decoded_token

                except Exception:
                    raise HTTPException(status_code=401, detail="Token inválido o expirado")

                return await func(request, *args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def assign_role(uid: str, role: str):
        if role not in ["superadmin", "doctor", "clinica"]:
            raise HTTPException(status_code=400, detail="Rol no válido")

        firebase_auth.set_custom_user_claims(uid, {"role": role})
        return {"message": f"Rol '{role}' asignado correctamente al usuario {uid}"}
