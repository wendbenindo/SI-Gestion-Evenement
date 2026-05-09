from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models, schemas
from fastapi import HTTPException, status

# ========== EVENTS ==========

def get_events(db: Session, search: str = None, date: str = None):
    """Récupérer la liste des événements avec filtres optionnels"""
    query = db.query(models.Event)
    
    if search:
        query = query.filter(models.Event.title.contains(search))
    
    if date:
        query = query.filter(models.Event.date >= date)
    
    return query.all()


def get_event(db: Session, event_id: int):
    """Récupérer un événement par ID"""
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Événement non trouvé"
        )
    return event


def create_event(db: Session, event: schemas.EventCreate):
    """Créer un nouvel événement"""
    db_event = models.Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def update_event(db: Session, event_id: int, event: schemas.EventCreate):
    """Mettre à jour un événement"""
    db_event = get_event(db, event_id)
    
    for key, value in event.model_dump().items():
        setattr(db_event, key, value)
    
    db.commit()
    db.refresh(db_event)
    return db_event


def delete_event(db: Session, event_id: int):
    """Supprimer un événement et ses inscriptions"""
    db_event = get_event(db, event_id)
    db.delete(db_event)
    db.commit()
    return {"message": "Événement supprimé"}


# ========== REGISTRATIONS ==========

def get_registrations(db: Session, event_id: int):
    """Récupérer les inscriptions d'un événement"""
    return db.query(models.Registration).filter(
        models.Registration.event_id == event_id
    ).all()


def create_registration(db: Session, event_id: int, registration: schemas.RegistrationCreate):
    """Créer une inscription avec validation métier"""
    
    # Vérifier que l'événement existe
    event = get_event(db, event_id)
    
    # Règle 1 : Vérifier la capacité
    current_registrations = db.query(models.Registration).filter(
        models.Registration.event_id == event_id
    ).count()
    
    if current_registrations >= event.capacity:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "error": "CAPACITY_REACHED",
                "message": "Cet événement est complet."
            }
        )
    
    # Règle 2 : Vérifier l'unicité de l'email pour cet événement
    existing_registration = db.query(models.Registration).filter(
        and_(
            models.Registration.event_id == event_id,
            models.Registration.email == registration.email
        )
    ).first()
    
    if existing_registration:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "error": "DUPLICATE_EMAIL",
                "message": "Cette adresse email est déjà enregistrée pour cet événement."
            }
        )
    
    # Créer l'inscription
    db_registration = models.Registration(
        event_id=event_id,
        **registration.model_dump()
    )
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration


def delete_registration(db: Session, registration_id: int):
    """Annuler une inscription"""
    db_registration = db.query(models.Registration).filter(
        models.Registration.id == registration_id
    ).first()
    
    if not db_registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inscription non trouvée"
        )
    
    db.delete(db_registration)
    db.commit()
    return {"message": "Inscription annulée"}
