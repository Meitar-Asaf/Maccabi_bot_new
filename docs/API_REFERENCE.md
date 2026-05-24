# API Reference

Base URL:
- Local: `http://localhost:8000`
- Cloud: `https://<backend-domain>`

API Prefix:
- `/api`

## Health
### GET `/health`
Returns service health.

Response:
```json
{ "status": "ok" }
```

## Root
### GET `/`
Returns service metadata.

## Subscriptions
### POST `/api/subscriptions`
Create/update subscriber.

Request:
```json
{
  "phone_e164": "+9725XXXXXXXX",
  "display_name": "Fan Name"
}
```

Response:
```json
{
  "id": "uuid",
  "phone_e164": "+9725XXXXXXXX",
  "whatsapp_status": "pending_opt_in"
}
```

### POST `/api/subscriptions/unsubscribe`
Unsubscribe by phone.

Request:
```json
{
  "phone_e164": "+9725XXXXXXXX"
}
```

Response:
```json
{
  "id": "uuid",
  "phone_e164": "+9725XXXXXXXX",
  "whatsapp_status": "unsubscribed"
}
```

Errors:
- `404` if subscriber does not exist.

## Players
### GET `/api/players/active`
Returns active and non-loaned players only.

Response item:
```json
{
  "id": "uuid",
  "full_name": "Player Name",
  "photo_url": "https://...",
  "goals_scored": 0,
  "games_played": 0,
  "successful_tackles": 0,
  "successful_passes": 0
}
```

## Admin
### GET `/api/admin/subscribers/summary`
Returns counts by key subscriber statuses.

### GET `/api/admin/notifications/jobs`
Returns queue/processing/failed/sent totals.

### POST `/api/admin/poll-live`
Triggers one live polling cycle.

Response:
```json
{ "created_jobs": 0 }
```

### POST `/api/admin/process-notifications`
Triggers due notification processing.

Response:
```json
{ "sent": 0, "retried": 0, "failed": 0 }
```

### GET `/api/admin/matches/live`
Returns currently live/in-progress matches.

## Webhooks
### POST `/api/webhooks/whatsapp/inbound`
Inbound WhatsApp keyword handling.

Request:
```json
{
  "phone_e164": "+9725XXXXXXXX",
  "message_text": "start"
}
```

Behavior:
- `start|subscribe|join` -> status `active`.
- `stop|unsubscribe|leave` -> status `unsubscribed`.
