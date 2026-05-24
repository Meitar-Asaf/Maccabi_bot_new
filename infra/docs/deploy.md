# Cloud Deployment (No local runtime)

## 1) Supabase (DB)
1. Create a free Supabase project.
2. Run SQL files in order from `infra/schema`:
   - `001_users.sql`
   - `002_players.sql`
   - `003_matches.sql`
   - `004_match_events.sql`
   - `005_notification_jobs.sql`
   - `006_message_deliveries.sql`
3. Copy your Supabase Postgres connection string.

## 2) Backend on Render
1. Connect your GitHub repo to Render.
2. Render will auto-detect `render.yaml` in project root.
3. In `maccabi-fan-api` environment variables, set:
   - `DATABASE_URL` = Supabase SQLAlchemy URL format, e.g.
     `postgresql+psycopg://USER:PASSWORD@HOST:5432/postgres`
   - `SPORTS_API_BASE_URL`
   - `SPORTS_API_KEY`
   - `WHATSAPP_PROVIDER`
   - `WHATSAPP_ACCESS_TOKEN`
   - `WHATSAPP_PHONE_NUMBER_ID`
   - `CORS_ALLOWED_ORIGINS` = your Vercel frontend URL
4. Deploy and verify:
   - `https://<render-app>/health`
   - `https://<render-app>/api/players/active`

## 3) Frontend on Vercel
1. Import the same GitHub repo in Vercel.
2. Set **Root Directory** to `frontend`.
3. Add env var:
   - `VITE_API_BASE_URL` = `https://<render-app>/api`
4. Deploy and open your Vercel URL.

## 4) Runtime checks
- Subscribe test: `POST /api/subscriptions`
- Unsubscribe test: `POST /api/subscriptions/unsubscribe`
- Poll trigger (manual): `POST /api/admin/poll-live`
- Process jobs (manual): `POST /api/admin/process-notifications`

## Notes
- Render cron services in `render.yaml` run poll + notification workers each minute.
- WhatsApp and some sports APIs may still have usage costs in production.
