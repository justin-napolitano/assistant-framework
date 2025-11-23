# assistant-core

Signal-driven personal assistant leveraging FastAPI and LangChain. This service integrates with signal-cli-rest-api to receive Signal messages, routes commands to various tools or an LLM, and replies via a notifier gateway.

---

## Features

- Signal message polling and handling
- Command support including `/help`, `/status`, `/weather [city]`, `/run <cmd>`, and `/ask <question>`
- Integration with LangChain and OpenAI for enhanced assistant capabilities
- Tooling for safe shell command execution and weather lookup
- Optional Retrieval-Augmented Generation (RAG) for querying local documents
- Dockerized for easy deployment

## Tech Stack

- Python 3
- FastAPI for HTTP API
- LangChain and OpenAI API for language model interactions
- signal-cli-rest-api for Signal messaging
- HTTPX for async HTTP requests
- Docker and Docker Compose for containerization

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- A running Signal stack accessible via environment variables
- OpenAI API key if you want LLM features

### Installation & Running

1. Copy `.env.example` to `.env` and fill in required values such as `SIGNAL_NUMBER`, `GATEWAY_TOKEN`, and optionally `OPENAI_API_KEY`.

```bash
cp .env.example .env
# Edit .env to add your configuration
```

2. Build and start the assistant-core service:

```bash
make run
```

3. To view logs:

```bash
make logs
```

## Project Structure

```
.
├── agent.py            # Core assistant agent logic integrating tools and LLM
├── app.py              # Application entry and orchestration
├── docker-compose.yml  # Docker Compose service definition
├── Dockerfile          # Docker image build instructions
├── Makefile            # Convenience commands
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── rag/                # Retrieval-Augmented Generation indexer and settings
├── services/           # External service clients (e.g., weather client)
├── tools/              # Tool implementations (shell commands, weather tool)
└── zzzzzzap.py         # FastAPI app handling Signal message polling and routing
```

## Commands Supported in Signal

- `/help` - Show help menu
- `/status` - Service heartbeat
- `/weather [city]` - Get current weather for a city
- `/run <cmd>` - Run whitelisted shell commands (e.g., uptime, df, docker-ps)
- `/ask <question>` - Query local documents using RAG (if enabled)

## Environment Variables

All configuration is read from `.env`. See `.env.example` for details. Key variables include:

- `SIGNAL_NUMBER` - Signal phone number
- `GATEWAY_TOKEN` - Authorization token for notifier gateway
- `NOTIFY_URL` - URL to send Signal replies
- `DISABLE_RAG` - Enable or disable document querying
- `OPENAI_API_KEY` - OpenAI API key for LLM

## Future Work / Roadmap

- Expand supported commands and tools
- Improve RAG integration with more document formats
- Add user authentication and access control
- Enhance error handling and logging
- Provide a web dashboard for monitoring and configuration
- Add tests and CI/CD pipeline

---

*This project assumes you have a working Signal CLI REST API and notifier gateway running separately.*
