from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import  empresa_admin_router, auth_router, empresa_public_router, doctor_independiente_router, doctor_admin_router, doctor_empresa_router

app = FastAPI(title="MediScan Backend", debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(empresa_admin_router.router)
app.include_router(auth_router.router)
app.include_router(empresa_public_router.router)
app.include_router(doctor_independiente_router.router)
app.include_router(doctor_admin_router.router)
app.include_router(doctor_empresa_router.router)

@app.get("/")
def root():
    return {"message": "MediScan API funcionando correctamente 🚀"}
