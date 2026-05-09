from fastapi import FastAPI
from .database import engine
from . import models

# Créer les tables automatiquement au démarrage
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Event Management API",
    description="API pour la gestion d'événements et d'inscriptions",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Event Management API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
