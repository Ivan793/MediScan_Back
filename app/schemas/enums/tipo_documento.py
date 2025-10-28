from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, ConfigDict


class TipoDocumentoEnum(str, Enum):
    CC = "Cédula de Ciudadanía"
    TI = "Tarjeta de Identidad"
    CE = "Cédula de Extranjería"
    PAS = "Pasaporte"
    NIT = "NIT"
