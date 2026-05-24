# Frontend (React + Vite)

## Purpose
Fan-facing dashboard:
- Landing page
- Subscribe/unsubscribe forms
- Active player statistics page
- Basic admin metrics page

## Local Run
```bash
npm install
npm run dev
```

## Build
```bash
npm run build
npm run preview
```

## Environment Variables
- `VITE_API_BASE_URL`
  - Example: `https://<backend-domain>/api`
  - Default fallback in code: `http://localhost:8000/api`

## Routes
- `/`
- `/subscribe`
- `/unsubscribe`
- `/players`
- `/admin`

## Data Contract
Players page expects each player object to include:
- `id`
- `full_name`
- `photo_url`
- `goals_scored`
- `games_played`
- `successful_tackles`
- `successful_passes`

## Notes
- Admin page currently shows basic stats but is not protected yet.
- All API calls are centralized in `src/lib/api.ts`.
