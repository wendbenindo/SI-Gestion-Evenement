from pydantic import BaseModel, EmailStr, Field, ConfigDict
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
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

# REGISTRATION SCHEMAS 

class RegistrationBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationResponse(RegistrationBase):
    id: int
    event_id: int
    registered_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
