from datetime import datetime

from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    industry: str | None = None


class ContactCreate(BaseModel):
    full_name: str
    email: str | None = None
    phone: str | None = None
    role: str | None = None
    company_id: int | None = None


class CandidateCreate(BaseModel):
    full_name: str
    stage: str = "sourced"
    owner: str | None = None


class NoteCreate(BaseModel):
    body: str
    note_type: str = "candidate"
    contact_id: int | None = None
    company_id: int | None = None


class TaskCreate(BaseModel):
    title: str
    due_at: datetime | None = None
    reminder_at: datetime | None = None
    status: str = "open"
    contact_id: int | None = None
