import firebase_admin
from firebase_admin import credentials, firestore
import os

# Ruta al archivo de credenciales (sube 2 niveles hasta el root)
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Ruta al archivo de credenciales (sube dos niveles desde /core)
cred_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "firebase_key.json")

# Inicializar Firebase solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Cliente Firestore
firebase_client = firestore.client()


# Inicializar Firebase solo una vez
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Cliente Firestore
firebase_client = firestore.client()
