# VIS-Recruit Operating System (MVP)

A modular business operating system for VIS-Recruit, designed with clean architecture and extension points.

## Modules

### 1) CRM
- Contacts and companies
- Candidate pipeline stages
- Client/candidate notes
- Tasks and reminders

### 2) Knowledge Base
- Store ISO 9001 procedures, forms, records, and files as structured documents
- Category, tags, owner, issue/review dates
- Version history with snapshots
- Full-text style search (SQLite `LIKE` based for MVP)
- Architecture prepared for future semantic search / AI QA via service layer and versioned content

### 3) Communications Hub
- Unified timeline of communication events
- Adapter architecture for:
  - Email
  - WhatsApp
  - Telegram
  - Viber
  - Facebook Messenger
  - Instagram
- MVP includes placeholder adapters/interfaces to keep channel integrations isolated

### 4) Audit & Compliance
- Document version history
- User action logs
- Timestamps and traceability for key actions

## Tech Stack
- FastAPI backend
- SQLite (MVP)
- SQLAlchemy ORM
- Simple static frontend

## Project Structure

```
app/
  api/              # Route modules per business capability
  core/             # DB and shared infrastructure
  integrations/     # External channel adapter interfaces/placeholders
  models/           # ORM entities
  schemas/          # Request payloads
  services/         # Business logic (versioning/search/audit)
  static/           # Minimal frontend
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
uvicorn app.main:app --reload
```

4. Open:
- App UI: `http://127.0.0.1:8000/`
- API docs: `http://127.0.0.1:8000/docs`

## Extension guidance

- Add new channels by implementing `ChannelAdapter` in `app/integrations/channels.py`.
- Add semantic search by introducing an embeddings store and retrieval service behind `KnowledgeService`.
- Migrate SQLite to PostgreSQL later by changing DB URL and adding migrations.
