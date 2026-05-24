# Backend (FastAPI)

## Run
```bash
python -m venv .venv
. .venv/Scripts/Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Worker commands
```bash
python -m app.workers.run_poll_once
python -m app.workers.run_notifications_once
```

## Main endpoints
- `POST /api/subscriptions`
- `POST /api/subscriptions/unsubscribe`
- `GET /api/players/active`
- `POST /api/admin/poll-live`
- `POST /api/admin/process-notifications`
- `POST /api/webhooks/whatsapp/inbound`
