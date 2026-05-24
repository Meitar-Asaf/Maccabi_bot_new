# Operations Runbook

## Daily Checks
- API health: `GET /health`
- Active players endpoint: `GET /api/players/active`
- Job queue summary: `GET /api/admin/notifications/jobs`
- Subscriber summary: `GET /api/admin/subscribers/summary`

## Manual Recovery Actions
### Trigger live polling once
```bash
curl -X POST https://<backend-domain>/api/admin/poll-live
```

### Process notifications once
```bash
curl -X POST https://<backend-domain>/api/admin/process-notifications
```

## Common Issues
### 1) No messages are sent
Check:
- Are there users with `whatsapp_status='active'`?
- Are jobs in `notification_jobs` with status `queued`/`retry`?
- Are cron workers running each minute?
- Are WhatsApp credentials configured?

### 2) Players page is empty
Check:
- `players` table has rows?
- `is_active=true` and `is_loaned_out=false`?
- `VITE_API_BASE_URL` points to correct backend?

### 3) CORS error in browser
Check:
- `CORS_ALLOWED_ORIGINS` includes frontend domain.
- Backend redeployed after env update.

## Logging Recommendations
- Log external provider response codes (sports/highlights/WhatsApp).
- Log job transitions: `queued -> processing -> sent/retry/failed`.
- Log webhook inputs (without leaking sensitive data).

## Backups
- Use your PostgreSQL provider backup policy.
- Keep periodic database dump snapshots.

## Security Baseline
- Store secrets only in cloud env vars.
- Enforce least-privilege DB user when possible.
- Add admin auth before exposing admin routes publicly.
