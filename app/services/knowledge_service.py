from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.entities import DocumentVersion, KnowledgeDocument


class KnowledgeService:
    @staticmethod
    def create_document(db: Session, payload):
        document = KnowledgeDocument(**payload.model_dump())
        db.add(document)
        db.flush()
        version = DocumentVersion(
            document_id=document.id,
            version=1,
            content_snapshot=document.content,
            changed_by=document.owner or "system",
        )
        db.add(version)
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def update_document(db: Session, document: KnowledgeDocument, payload):
        data = payload.model_dump(exclude_none=True)
        changed_by = data.pop("changed_by", "system")
        for key, value in data.items():
            setattr(document, key, value)
        last_version = document.versions[-1].version if document.versions else 0
        if "content" in data:
            db.add(
                DocumentVersion(
                    document_id=document.id,
                    version=last_version + 1,
                    content_snapshot=document.content,
                    changed_by=changed_by,
                )
            )
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def search_documents(db: Session, query: str):
        pattern = f"%{query}%"
        return (
            db.query(KnowledgeDocument)
            .filter(
                or_(
                    KnowledgeDocument.title.ilike(pattern),
                    KnowledgeDocument.tags.ilike(pattern),
                    KnowledgeDocument.content.ilike(pattern),
                    KnowledgeDocument.category.ilike(pattern),
                )
            )
            .all()
        )
