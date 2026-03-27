from sqlalchemy.orm import Session

from app.models.entities import AuditLog


def log_action(
    db: Session,
    action: str,
    entity_type: str,
    entity_id: str | None = None,
    actor: str = "system",
    details: str | None = None,
):
    record = AuditLog(
        actor=actor,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        details=details,
    )
    db.add(record)
    db.commit()
