import firebase_admin
from firebase_admin import credentials, auth
import os

def init_firebase():
    if not firebase_admin._apps:
        cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH", "firebase_credentials.json")
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        print("Firebase inicializado correctamente")

    load_default_users()


def load_default_users():
    default_users = [
        {"email": "superadmin@demo.com", "password": "123456", "role": "superadmin"},
        {"email": "doctor@demo.com", "password": "123456", "role": "doctor"},
        {"email": "clinica@demo.com", "password": "123456", "role": "clinica"},
    ]

    for u in default_users:
        try:
            user = auth.get_user_by_email(u["email"])
            print(f"El usuario {u['email']} ya existe.")
        except auth.UserNotFoundError:
            user = auth.create_user(email=u["email"], password=u["password"])
            print(f" Usuario {u['email']} creado.")

        # Asignar rol si no coincide
        claims = user.custom_claims or {}
        if claims.get("role") != u["role"]:
            auth.set_custom_user_claims(user.uid, {"role": u["role"]})
            print(f"Rol '{u['role']}' asignado a {u['email']}.")
