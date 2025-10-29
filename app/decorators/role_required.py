from fastapi import Request, HTTPException, status
from firebase_admin import auth as firebase_auth
from functools import wraps

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
