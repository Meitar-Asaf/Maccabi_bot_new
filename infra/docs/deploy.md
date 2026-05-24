# Cloud Deployment (No local runtime)

## 1) PostgreSQL (DB)
1. Create a PostgreSQL database (provider of your choice).
2. Run SQL files in order from `infra/schema`:
   - `001_users.sql`
   - `002_players.sql`
   - `003_matches.sql`
   - `004_match_events.sql`
   - `005_notification_jobs.sql`
   - `006_message_deliveries.sql`
3. Copy your Postgres connection string.

Optional (PowerShell, one command):
```powershell
$env:DATABASE_URL="postgresql://USER:PASSWORD@HOST:5432/postgres?sslmode=require"
./infra/scripts/apply_schema.ps1
```

Example providers:
- Supabase (Postgres)
- Neon (Postgres)
- Render Postgres
- Any managed PostgreSQL service

## 2) Backend on Vercel (No card required)
1. Import the same GitHub repo in Vercel.
2. Create a **separate project** for backend with **Root Directory** = `backend`.
3. Vercel will use `backend/vercel.json` and `backend/api/index.py`.
4. In backend project Environment Variables, set:
   - `DATABASE_URL` = SQLAlchemy Postgres URL format, e.g.
     `postgresql+psycopg://USER:PASSWORD@HOST:5432/postgres`
   - `SPORTS_API_BASE_URL`
   - `SPORTS_API_KEY`
   - `WHATSAPP_PROVIDER`
   - `WHATSAPP_ACCESS_TOKEN`
   - `WHATSAPP_PHONE_NUMBER_ID`
   - `CORS_ALLOWED_ORIGINS` = your Vercel frontend URL
5. Deploy and verify:
   - `https://<backend-vercel-domain>/health`
   - `https://<backend-vercel-domain>/api/players/active`

## 2.1) Free scheduling via GitHub Actions (instead of Render Cron)
1. In GitHub repo settings, add secret:
   - `BACKEND_BASE_URL` = `https://<backend-vercel-domain>`
2. Workflow file `.github/workflows/scheduler.yml` triggers every 5 minutes:
   - `POST /api/admin/poll-live`
   - `POST /api/admin/process-notifications`
3. You can also run it manually from GitHub Actions using `workflow_dispatch`.

## 3) Frontend on Vercel
1. Import the same GitHub repo in Vercel.
2. Set **Root Directory** to `frontend`.
3. Add env var:
   - `VITE_API_BASE_URL` = `https://<backend-vercel-domain>/api`
4. Deploy and open your Vercel URL.

## 4) Runtime checks
- Subscribe test: `POST /api/subscriptions`
- Unsubscribe test: `POST /api/subscriptions/unsubscribe`
- Poll trigger (manual): `POST /api/admin/poll-live`
- Process jobs (manual): `POST /api/admin/process-notifications`

## Notes
- Scheduler is handled by GitHub Actions every 5 minutes for a no-cost path.
- WhatsApp and some sports APIs may still have usage costs in production.

## Optional: Render path
- If Render account allows deployment without billing block, you can still use `render.yaml`.
