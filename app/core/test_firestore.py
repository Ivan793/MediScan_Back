from app.core.firebase import firebase_client  # Ajusta la ruta si es diferente
from google.api_core.exceptions import GoogleAPICallError, RetryError

try:
    # Crear un documento de prueba en la colección "test_conexion"
    doc_ref = firebase_client.collection("test_conexion").document("prueba")
    doc_ref.set({"mensaje": "¡Conexión exitosa!"})
    
    # Leer el documento de vuelta
    doc = doc_ref.get()
    if doc.exists:
        print("✅ Conexión a Firestore OK:", doc.to_dict())
    else:
        print("❌ No se pudo leer el documento de prueba.")

except (GoogleAPICallError, RetryError) as e:
    print("❌ Error al conectar con Firestore:", e)
except Exception as e:
    print("❌ Otro error inesperado:", e)
