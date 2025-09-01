system_full - Fully implemented starter school system (backend + frontend)

Generated: 2025-09-01T14:27:03.897265 UTC

Quickstart (backend):
  cd backend
  python -m venv .venv
  source .venv/bin/activate    # Windows: .venv\Scripts\activate
  pip install -r requirements.txt
  cp .env.example .env
  python manage.py migrate
  python manage.py create_default_superuser
  python manage.py runserver

Quickstart (frontend):
  cd frontend
  npm install
  npm start

Notes:
- Backend uses sqlite by default; change to MySQL in backend/system_api/settings.py
- Set keys in backend/.env
- Media files stored in backend/media
