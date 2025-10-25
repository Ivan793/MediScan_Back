# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import  empresa_admin_router, empresa_public_router

app = FastAPI(title="MediScan Backend", debug=True)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers

app.include_router(empresa_admin_router.router)
app.include_router(empresa_public_router.router)

@app.get("/")
def root():
    return {"message": "MediScan API funcionando correctamente 🚀"}
