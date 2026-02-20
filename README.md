# Watch Pricing Intelligence Engine

A Python project scaffold for ingesting watch listings, normalizing data, and computing pricing/liquidity signals.

## Tech Stack

- **FastAPI** for backend APIs
- **Supabase PostgreSQL** (Postgres-compatible) for data storage
- **asyncpg** for async database access
- **OpenAI API** (skeleton integration) for title normalization

## Project Structure

```text
.
├── app
│   ├── api
│   │   └── routes.py
│   ├── db
│   │   └── supabase.py
│   ├── liquidity
│   │   └── score.py
│   ├── normalization
│   │   └── title_normalizer.py
│   ├── pricing
│   │   └── engine.py
│   ├── scrapers
│   │   ├── chrono24.py
│   │   └── ebay.py
│   ├── main.py
│   └── settings.py
├── .env.example
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Quick Start (Local)

1. Copy env file:

```bash
cp .env.example .env
```

2. Start services:

```bash
docker compose up --build
```

3. Check API health:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{"status":"ok"}
```

## Run Without Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

## Notes

- Scraper modules are placeholders and should be extended with robust error handling, retries, and anti-bot strategy.
- Normalization module includes a placeholder OpenAI client setup and a stub function.
- Pricing and liquidity modules include simple baseline functions for later expansion.
