# Free/Hobby Hosting Strategy

## Recommended
- Frontend: Vercel Hobby (React static build)
- Database/Auth: Supabase Free (PostgreSQL + Auth)
- Backend API/Worker: Render or similar hobby-tier Python service
- CI + nightly jobs: GitHub Actions

## Workload split
- Live match polling + notification processing should run on backend host scheduler (or cron endpoint).
- Nightly player sync and health checks can run on GitHub Actions.

## Cost boundary notes
- Production WhatsApp outbound messages may incur cost.
- Real-time sports APIs may require paid tiers for lower-latency live events.
