import os
from datetime import timedelta

SECRET_KEY = os.getenv("SECRET_KEY", "mi_clave_super_secreta")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30