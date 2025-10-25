from pydantic import constr, EmailStr
from typing import Literal, Optional
from datetime import date

# 🪪 Tipos de documento permitidos
UsuarioDocumentoTipo = Literal["CC", "CE", "TI", "PA"]

# 🧾 Identificación: solo números, de 6 a 12 dígitos
UsuarioIdentificacion = constr(pattern=r'^\d{6,12}$', strip_whitespace=True)

# 👤 Nombre/apellido: solo letras y espacios, 2–50 caracteres
UsuarioNombre = constr(pattern=r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]{2,50}$', strip_whitespace=True)

# 🚻 Género
UsuarioGenero = Optional[Literal["Masculino", "Femenino", "Otro"]]

# 🌍 País y ciudad: letras y espacios, 2–50 caracteres
UsuarioPais = Optional[constr(pattern=r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]{2,50}$', strip_whitespace=True)]
UsuarioCiudad = Optional[constr(pattern=r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]{2,50}$', strip_whitespace=True)]

# 🏠 Dirección: caracteres alfanuméricos y símbolos comunes, 5–100 caracteres
UsuarioDireccion = Optional[constr(pattern=r'^[\w\s#\-\.,]{5,100}$', strip_whitespace=True)]

# ☎️ Teléfono: números con longitud entre 7 y 15
UsuarioTelefono = Optional[constr(pattern=r'^\+?\d{7,15}$', strip_whitespace=True)]

# 📧 Email validado con Pydantic
UsuarioEmail = EmailStr

# 🔒 Contraseña con validación fuerte
UsuarioPassword = constr(
    pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{8,64}$',
    strip_whitespace=True
)

# 🎭 Rol de usuario
UsuarioRol = Literal["Admin", "Empresa", "Doctor", "Paciente"]

# 📅 Fecha de nacimiento
UsuarioFechaNacimiento = Optional[date]
