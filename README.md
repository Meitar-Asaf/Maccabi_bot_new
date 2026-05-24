# Maccabi Fan Platform

Monorepo for:
- `backend` (FastAPI + async workers)
- `frontend` (React + Vite)
- `infra` (PostgreSQL schema and deployment notes)

## Stack
- Python 3.12+, FastAPI, SQLAlchemy, Alembic-ready structure
- React + TypeScript + Vite
- PostgreSQL (any provider: local, Supabase, Neon, Render, etc.)

## Quick start
### 1) Backend
```bash
cd backend
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 2) Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3) Database
Run SQL files in `infra/schema` against your PostgreSQL database in this order:
1. `001_users.sql`
2. `002_players.sql`
3. `003_matches.sql`
4. `004_match_events.sql`
5. `005_notification_jobs.sql`
6. `006_message_deliveries.sql`

## Notes
- WhatsApp production messaging may incur costs; this repo keeps provider logic abstracted.
- Highlights are handled as URL/link references only.

## Cloud deploy
- Backend Vercel config: `backend/vercel.json`
- Backend entrypoint for Vercel: `backend/api/index.py`
- Frontend Vercel config: `frontend/vercel.json`
- Step-by-step guide: `infra/docs/deploy.md`

## Documentation Index
- System architecture: `docs/ARCHITECTURE.md`
- API reference: `docs/API_REFERENCE.md`
- Database reference: `docs/DATABASE.md`
- Environment variables: `docs/ENVIRONMENT_VARIABLES.md`
- Operations runbook: `docs/OPERATIONS.md`
- Backend quick guide: `backend/README.md`
- Frontend quick guide: `frontend/README.md`
