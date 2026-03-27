from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.entities import KnowledgeDocument
from app.schemas.knowledge import DocumentCreate, DocumentUpdate
from app.services.audit import log_action
from app.services.knowledge_service import KnowledgeService

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


@router.post("/documents")
def create_document(payload: DocumentCreate, db: Session = Depends(get_db)):
    doc = KnowledgeService.create_document(db, payload)
    log_action(db, "create", "knowledge_document", str(doc.id))
    return doc


@router.get("/documents")
def list_documents(db: Session = Depends(get_db)):
    return db.query(KnowledgeDocument).all()


@router.get("/documents/search")
def search_documents(query: str, db: Session = Depends(get_db)):
    return KnowledgeService.search_documents(db, query)


@router.patch("/documents/{document_id}")
def update_document(document_id: int, payload: DocumentUpdate, db: Session = Depends(get_db)):
    doc = db.query(KnowledgeDocument).filter(KnowledgeDocument.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    updated = KnowledgeService.update_document(db, doc, payload)
    log_action(db, "update", "knowledge_document", str(updated.id))
    return updated


@router.get("/documents/{document_id}/versions")
def list_versions(document_id: int, db: Session = Depends(get_db)):
    doc = db.query(KnowledgeDocument).filter(KnowledgeDocument.id == document_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc.versions
