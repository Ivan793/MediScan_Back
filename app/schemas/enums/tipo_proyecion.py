# app/enums/proyeccion_radiologica.py
from enum import Enum

class TipoProyeccion(str, Enum):
    PA = "PA"              
    AP = "AP"             
    LATERAL = "Lateral"
    AP_LATERAL = "AP-Lateral"
    OTRAS = "Otras"
