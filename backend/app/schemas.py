from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# EVENT SCHEMAS 

class EventBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = None
    date: datetime
    location: str
    capacity: int = Field(..., gt=0)

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int
    createdAt: datetime
    
    class Config:
        from_attributes = True
        # Alias pour convertir snake_case -> camelCase
        populate_by_name = True

# REGISTRATION SCHEMAS 

class RegistrationBase(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationResponse(RegistrationBase):
    id: int
    eventId: int
    registeredAt: datetime
    
    class Config:
        from_attributes = True
        populate_by_name = True
