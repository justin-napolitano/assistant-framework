# assistant-core

Signal-driven personal assistant (FastAPI + LangChain). Polls signal-cli-rest-api,
routes messages to tools/LLM, replies via your notifier-gateway.

## Quick start
1) Copy `.env.example` to `.env` and fill values.
2) `make run` — builds and starts only this service via docker compose.
3) `make logs` — tail logs.

> This compose file only includes assistant-core. It expects your signal stack
> to already be running and reachable via NOTIFY_URL / SIGNAL_API_BASE in `.env`.

## Commands in Signal
- `/help`
- `/status`
- `/weather [city]`
- `/run uptime|df|docker-ps`
- `/ask <question>` (enable RAG by mounting RAG_DATA_DIR and setting DISABLE_RAG=false)

## Environment
All configuration is read from `.env`. See `.env.example` for fields.
