# Veritas Backend

FastAPI backend for the Veritas evidence infrastructure platform.

## Structure

```
backend/
├── app/
│   ├── main.py          # FastAPI application entry point
│   ├── config.py        # Environment and app settings
│   ├── api/             # HTTP routes
│   ├── engine/          # Evidence Engine (core business logic)
│   ├── sources/         # External evidence sources (e.g. PubMed)
│   ├── schemas/         # Shared request/response schemas
│   └── workflows/       # Orchestration between API, engine, and sources
├── tests/
├── requirements.txt
└── .env.example
```

## Setup

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
```

## Run

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API docs: http://localhost:8000/docs

Health check: http://localhost:8000/api/v1/health

## Test

```bash
pytest
```
