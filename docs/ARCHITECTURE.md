# Architecture

## Overview
Maccabi Fan Platform is a monorepo with three parts:
- `backend`: FastAPI API, integration adapters, and background workers.
- `frontend`: React dashboard (Vite) for fan subscription and player stats.
- `infra`: PostgreSQL schema and deployment documentation.

## High-Level Flow
1. Fans submit phone numbers from the frontend.
2. Backend stores subscription state in PostgreSQL.
3. Live polling worker checks sports events.
4. New goal events are deduplicated and stored.
5. A delayed notification job is scheduled for ~2 minutes.
6. Notification worker attempts highlight lookup.
7. Backend sends WhatsApp updates to active subscribers.
8. Delivery outcomes are saved per user and job.

## Components
### Backend API
- Framework: FastAPI.
- Prefix: `/api` (configurable).
- Public endpoints:
  - Subscribe / unsubscribe.
  - Active player list.
- Admin endpoints:
  - Live polling trigger.
  - Notification processing trigger.
  - Subscriber/job summaries.

### Backend Services
- `subscriptions.py`: add/update/unsubscribe subscriber records.
- `players.py`: active player filtering (`is_active=true`, `is_loaned_out=false`).
- `live_matches.py`: poll + dedupe goal events + create delayed jobs.
- `notifications.py`: process due jobs, resolve highlights, send WhatsApp, store delivery logs.

### Integrations (Adapters)
- `sports_client.py`: live events and match stats provider abstraction.
- `highlight_resolver.py`: highlight link discovery abstraction.
- `whatsapp_client.py`: outbound WhatsApp provider abstraction.

### Workers
- `app.workers.run_poll_once`: executes one live-poll cycle.
- `app.workers.run_notifications_once`: executes one due-job processing cycle.
- Production schedule: every minute (configured in `render.yaml`).

### Frontend
- React app routes:
  - `/`: landing page
  - `/subscribe`: subscribe form
  - `/unsubscribe`: unsubscribe form
  - `/players`: active player cards
  - `/admin`: basic admin metrics view
- API base URL configured via `VITE_API_BASE_URL`.

## Design Decisions
- PostgreSQL as source of truth.
- Idempotency by external event ID and one job per goal event.
- Delay before highlight lookup to reduce missing-link failures.
- Link/embed-only highlights (no clip file hosting).
- Adapter pattern for provider swap (sports/WhatsApp/highlights).

## Known Production Gaps (Current Scaffold)
- Mock integrations are placeholders until real provider credentials + implementations are added.
- Admin page is not yet auth-protected in UI.
- No rate-limiting/multi-tenant controls yet.
