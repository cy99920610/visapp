from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.integrations.channels import ADAPTER_REGISTRY
from app.models.entities import CommunicationEvent
from app.schemas.communications import CommunicationCreate
from app.services.audit import log_action

router = APIRouter(prefix="/communications", tags=["communications"])


@router.post("/events")
def create_event(payload: CommunicationCreate, db: Session = Depends(get_db)):
    if payload.channel not in ADAPTER_REGISTRY:
        raise HTTPException(status_code=400, detail="Unsupported channel")
    event = CommunicationEvent(**payload.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    log_action(db, "create", "communication_event", str(event.id))
    return event


@router.get("/timeline")
def unified_timeline(contact_id: int | None = None, company_id: int | None = None, db: Session = Depends(get_db)):
    query = db.query(CommunicationEvent)
    if contact_id is not None or company_id is not None:
        query = query.filter(
            or_(
                CommunicationEvent.contact_id == contact_id,
                CommunicationEvent.company_id == company_id,
            )
        )
    return query.order_by(CommunicationEvent.created_at.desc()).all()


@router.get("/adapters")
def list_adapters():
    return list(ADAPTER_REGISTRY.keys())
