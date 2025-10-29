from fastapi import Header, HTTPException
from firebase_admin import auth as firebase_auth, exceptions

class AuthServicio:

    @staticmethod
    def get_current_user(authorization: str = Header(None)):
        if not authorization:
            raise HTTPException(status_code=401, detail="Token no proporcionado")

        try:
            token = authorization.split(" ")[1]
            decoded_token = firebase_auth.verify_id_token(token)
            uid = decoded_token.get("uid")

            user = firebase_auth.get_user(uid)

            return {
                "uid": user.uid,
                "email": user.email,
                "role": decoded_token.get("role"),
                "display_name": user.display_name,
                "email_verified": user.email_verified,
                "phone_number": user.phone_number,
                "photo_url": user.photo_url
            }

        except exceptions.FirebaseError:
            raise HTTPException(status_code=401, detail="Token inválido o expirado")

    @staticmethod
    def assign_role(uid: str, role: str):
        if role not in ["superadmin", "doctor", "clinica"]:
            raise HTTPException(status_code=400, detail="Rol no válido")

        firebase_auth.set_custom_user_claims(uid, {"role": role})
        return {"message": f"Rol '{role}' asignado correctamente al usuario {uid}"}
