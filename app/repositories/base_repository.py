from typing import Any, Dict, List, Optional
from datetime import datetime
import logging
from google.cloud import firestore

from app.core.firebase import get_firestore_client

logger = logging.getLogger(__name__)


class BaseRepository:
    """
    Clase base genérica para interactuar con una colección de Firestore.
    Permite operaciones CRUD básicas y filtrado.
    """

    def __init__(self, collection_name: str, id_field: str = "id"):
        self.db = get_firestore_client()
        self.collection = self.db.collection(collection_name)
        self.id_field = id_field
        self.collection_name = collection_name

    # -------------------------------
    # 🔹 Crear documento
    # -------------------------------
    async def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Crea un nuevo documento en la colección y devuelve los datos creados.
        """
        doc_ref = self.collection.document()
        data[self.id_field] = doc_ref.id
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()

        doc_ref.set(data)
        logger.info(f"Documento creado en {self.collection_name}: {doc_ref.id}")
        return data

    # -------------------------------
    # 🔹 Obtener documento por ID
    # -------------------------------
    async def get_by_id(self, doc_id: str) -> Optional[Dict[str, Any]]:
        doc = self.collection.document(doc_id).get()
        if doc.exists:
            return doc.to_dict()
        return None

    # -------------------------------
    # 🔹 Obtener todos (opcionalmente con filtros)
    # -------------------------------
    async def get_all(self, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        query = self.collection
        if filters:
            for key, value in filters.items():
                query = query.where(key, "==", value)

        docs = query.stream()
        results = [doc.to_dict() for doc in docs]
        return results

    # -------------------------------
    # 🔹 Buscar por campo específico
    # -------------------------------
    async def get_by_field(self, field: str, value: Any) -> Optional[Dict[str, Any]]:
        docs = self.collection.where(field, "==", value).limit(1).stream()
        for doc in docs:
            return doc.to_dict()
        return None

    # -------------------------------
    # 🔹 Actualizar documento
    # -------------------------------
    async def update(self, doc_id: str, data: Dict[str, Any]) -> bool:
        """
        Actualiza un documento existente.
        """
        doc_ref = self.collection.document(doc_id)
        if not doc_ref.get().exists:
            logger.warning(f"Documento {doc_id} no encontrado en {self.collection_name}")
            return False

        data["updated_at"] = datetime.utcnow()
        doc_ref.update(data)
        logger.info(f"Documento actualizado en {self.collection_name}: {doc_id}")
        return True

    # -------------------------------
    # 🔹 Eliminar documento
    # -------------------------------
    async def delete(self, doc_id: str) -> bool:
        """
        Elimina un documento de la colección.
        """
        doc_ref = self.collection.document(doc_id)
        if not doc_ref.get().exists:
            logger.warning(f"Documento {doc_id} no encontrado en {self.collection_name}")
            return False

        doc_ref.delete()
        logger.info(f"Documento eliminado de {self.collection_name}: {doc_id}")
        return True
