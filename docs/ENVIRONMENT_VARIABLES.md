# Environment Variables

## Backend
Defined in `backend/app/core/config.py`.

Required for production:
- `DATABASE_URL`
- `SPORTS_API_BASE_URL`
- `SPORTS_API_KEY`
- `WHATSAPP_PROVIDER`
- `WHATSAPP_ACCESS_TOKEN`
- `WHATSAPP_PHONE_NUMBER_ID`
- `CORS_ALLOWED_ORIGINS`

Optional/with defaults:
- `APP_NAME` (default: `Maccabi Fan Platform API`)
- `API_PREFIX` (default: `/api`)
- `ENVIRONMENT` (default: `development`)
- `HIGHLIGHT_SEARCH_DELAY_SECONDS` (default: `120`)
- `MATCH_POLL_INTERVAL_SECONDS` (default: `60`)

Example:
```dotenv
APP_NAME="Maccabi Fan Platform API"
API_PREFIX="/api"
ENVIRONMENT="production"
DATABASE_URL="postgresql+psycopg://USER:PASSWORD@HOST:5432/postgres"
SPORTS_API_BASE_URL="https://provider.example"
SPORTS_API_KEY="YOUR_KEY"
WHATSAPP_PROVIDER="meta"
WHATSAPP_ACCESS_TOKEN="YOUR_TOKEN"
WHATSAPP_PHONE_NUMBER_ID="YOUR_PHONE_NUMBER_ID"
CORS_ALLOWED_ORIGINS="https://your-vercel-app.vercel.app"
```

## Frontend
Used by Vite.

- `VITE_API_BASE_URL`
  - Example: `https://<backend-domain>/api`
