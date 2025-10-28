from enum import Enum

class EstadoCivilEnum(str, Enum):
    SOLTERO = "Soltero"
    CASADO = "Casado"
    UNION_LIBRE = "Unión libre"
    DIVORCIADO = "Divorciado"
    VIUDO = "Viudo"
    SEPARADO = "Separado"
