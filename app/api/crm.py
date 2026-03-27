from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.entities import Candidate, Company, Contact, Note, Task
from app.schemas.crm import CandidateCreate, CompanyCreate, ContactCreate, NoteCreate, TaskCreate
from app.services.audit import log_action

router = APIRouter(prefix="/crm", tags=["crm"])


@router.post("/companies")
def create_company(payload: CompanyCreate, db: Session = Depends(get_db)):
    company = Company(**payload.model_dump())
    db.add(company)
    db.commit()
    db.refresh(company)
    log_action(db, "create", "company", str(company.id))
    return company


@router.get("/companies")
def list_companies(db: Session = Depends(get_db)):
    return db.query(Company).all()


@router.post("/contacts")
def create_contact(payload: ContactCreate, db: Session = Depends(get_db)):
    contact = Contact(**payload.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    log_action(db, "create", "contact", str(contact.id))
    return contact


@router.get("/contacts")
def list_contacts(db: Session = Depends(get_db)):
    return db.query(Contact).all()


@router.post("/candidates")
def create_candidate(payload: CandidateCreate, db: Session = Depends(get_db)):
    candidate = Candidate(**payload.model_dump())
    db.add(candidate)
    db.commit()
    db.refresh(candidate)
    log_action(db, "create", "candidate", str(candidate.id))
    return candidate


@router.get("/candidates")
def list_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()


@router.post("/notes")
def create_note(payload: NoteCreate, db: Session = Depends(get_db)):
    note = Note(**payload.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    log_action(db, "create", "note", str(note.id))
    return note


@router.get("/notes")
def list_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()


@router.post("/tasks")
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    task = Task(**payload.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)
    log_action(db, "create", "task", str(task.id))
    return task


@router.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()
