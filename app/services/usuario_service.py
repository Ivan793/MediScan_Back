from typing import List, Optional
from app.schemas.usuario import UsuarioCrear, UsuarioRespuesta
import uuid

class UsuarioServicio:
    _usuarios: List[UsuarioRespuesta] = []

    @classmethod
    def crear_usuario(cls, datos_usuario: UsuarioCrear) -> UsuarioRespuesta:
        """
        Crea un nuevo usuario verificando que el correo y el documento no estén duplicados.
        """
        # Validar duplicados
        for usuario in cls._usuarios:
            if usuario.correo == datos_usuario.correo:
                raise ValueError("El correo electrónico ya está registrado.")
            if usuario.numero_documento == datos_usuario.numero_documento:
                raise ValueError("El número de documento ya está registrado.")

        # Crear usuario
        nuevo_usuario = UsuarioRespuesta(
            id=str(uuid.uuid4()),
            nombre=datos_usuario.nombre,
            correo=datos_usuario.correo,
            numero_documento=datos_usuario.numero_documento
        )
        cls._usuarios.append(nuevo_usuario)
        return nuevo_usuario

    @classmethod
    def obtener_todos_los_usuarios(cls) -> List[UsuarioRespuesta]:
        """
        Retorna la lista completa de usuarios registrados.
        """
        return cls._usuarios.copy()

    @classmethod
    def obtener_usuario_por_id(cls, usuario_id: str) -> Optional[UsuarioRespuesta]:
        """
        Busca un usuario por su ID.
        """
        for usuario in cls._usuarios:
            if usuario.id == usuario_id:
                return usuario
        raise ValueError("Usuario no encontrado.")

    @classmethod
    def eliminar_usuario(cls, usuario_id: str) -> bool:
        """
        Elimina un usuario por su ID.
        """
        for i, usuario in enumerate(cls._usuarios):
            if usuario.id == usuario_id:
                cls._usuarios.pop(i)
                return True
        raise ValueError("No se pudo eliminar el usuario. ID no encontrado.")
