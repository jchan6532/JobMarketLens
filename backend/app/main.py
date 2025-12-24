#Developers: Justin Chan, Philip Wojdyna
#Date: December 18, 2025
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.ingestion import router as ingestion_router
from app.api.job import router as job_router
from app.api.analytic import router as analytic_router
from app.api.admin import router as admin_router

app = FastAPI(
    title="JobMarketLens API",
    version="1.0.0",
    description="Backend for JobMarketLens API."
)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingestion_router)
app.include_router(job_router)
app.include_router(analytic_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return "default"

@app.get("/health")
def health():
    return {"status": "ok"}
