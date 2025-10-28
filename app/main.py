# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import (
    empresa_admin_router,
    empresa_public_router,
    doctor_independiente_router,
    doctor_admin_router,
    doctor_empresa_router
)

app = FastAPI(title="MediScan Backend", debug=True)

# 🔹 Configuración CORS (Modificada aquí)
origins = [
    "http://localhost:5173",  # ← frontend local de React (Vite)
    "http://127.0.0.1:5173",  # ← otra forma local
    "https://tudominio-frontend.com"  # ← opcional: dominio en producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # ← restringimos solo a nuestros orígenes válidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Routers
app.include_router(empresa_admin_router.router)
app.include_router(empresa_public_router.router)
app.include_router(doctor_independiente_router.router)
app.include_router(doctor_admin_router.router)
app.include_router(doctor_empresa_router.router)

# 🔹 Endpoint raíz
@app.get("/")
def root():
    return {"message": "MediScan API funcionando correctamente 🚀"}
