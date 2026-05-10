from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Optional, List
from .database import engine, get_db
from . import models, schemas, crud

# Créer les tables automatiquement au démarrage
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Event Management API",
    description="API pour la gestion d'événements et d'inscriptions",
    version="1.0.0"
)

# Configuration CORS - Plus permissive
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permet toutes les origines (pour le dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Event Management API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


# endpoints evenments 

@app.get("/api/events", response_model=List[schemas.EventResponse])
def get_events(
    search: Optional[str] = Query(None, description="Recherche par titre"),
    date: Optional[str] = Query(None, description="Filtrer par date"),
    db: Session = Depends(get_db)
):
    """Récupérer la liste des événements avec filtres optionnels"""
    return crud.get_events(db, search=search, date=date)


@app.post("/api/events", response_model=schemas.EventResponse, status_code=201)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    """Créer un nouvel événement"""
    return crud.create_event(db, event)


@app.get("/api/events/{event_id}", response_model=schemas.EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    """Récupérer un événement par ID"""
    return crud.get_event(db, event_id)


@app.put("/api/events/{event_id}", response_model=schemas.EventResponse)
def update_event(event_id: int, event: schemas.EventCreate, db: Session = Depends(get_db)):
    """Mettre à jour un événement"""
    return crud.update_event(db, event_id, event)


@app.delete("/api/events/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    """Supprimer un événement"""
    return crud.delete_event(db, event_id)


# endpoints incriptions

@app.post("/api/events/{event_id}/register", response_model=schemas.RegistrationResponse, status_code=201)
def register_to_event(
    event_id: int,
    registration: schemas.RegistrationCreate,
    db: Session = Depends(get_db)
):
    """Inscrire un participant à un événement"""
    return crud.create_registration(db, event_id, registration)


@app.get("/api/events/{event_id}/registrations", response_model=List[schemas.RegistrationResponse])
def get_event_registrations(event_id: int, db: Session = Depends(get_db)):
    """Récupérer la liste des participants d'un événement"""
    return crud.get_registrations(db, event_id)


@app.delete("/api/registrations/{registration_id}")
def cancel_registration(registration_id: int, db: Session = Depends(get_db)):
    """Annuler une inscription"""
    return crud.delete_registration(db, registration_id)
