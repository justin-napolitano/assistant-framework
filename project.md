---
slug: github-assistant-framework
id: github-assistant-framework
title: assistant-core
repo: justin-napolitano/assistant-framework
githubUrl: https://github.com/justin-napolitano/assistant-framework
generatedAt: '2025-11-24T21:33:59.442Z'
source: github-auto
summary: >-
  Signal-driven personal assistant service built using FastAPI and LangChain. It
  integrates with signal-cli-rest-api to receive Signal messages, processes
  commands via various tools or a large language model (LLM), and responds
  through a notifier gateway.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

Signal-driven personal assistant service built using FastAPI and LangChain. It integrates with signal-cli-rest-api to receive Signal messages, processes commands via various tools or a large language model (LLM), and responds through a notifier gateway.

---

## Features

- Polls and handles Signal messages asynchronously
- Supports commands such as `/help`, `/status`, `/weather [city]`, `/run <cmd>`, and `/ask <question>`
- Integrates LangChain and OpenAI API for enhanced language model capabilities
- Provides tooling for safe shell command execution and weather information retrieval
- Optional Retrieval-Augmented Generation (RAG) for querying local document indexes
- Fully containerized with Docker and Docker Compose for straightforward deployment

## Tech Stack

- Python 3
- FastAPI for HTTP API
- LangChain and OpenAI API for language model interactions
- signal-cli-rest-api for Signal messaging integration
- HTTPX for asynchronous HTTP requests
- Docker and Docker Compose for containerization

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Access to a Signal stack configured via environment variables
- OpenAI API key if LLM features are desired

### Installation & Running

1. Copy `.env.example` to `.env` and configure required environment variables such as `SIGNAL_NUMBER`, `GATEWAY_TOKEN`, and optionally `OPENAI_API_KEY`.

```bash
cp .env.example .env
# Edit .env to add your configuration
```

2. Build and start the assistant-core service using Makefile convenience commands:

```bash
make run
```

3. To view service logs:

```bash
make logs
```

## Project Structure

```
.
├── agent.py            # Core assistant agent logic integrating tools and LLM
├── app.py              # Application entry point and orchestration
├── docker-compose.yml  # Docker Compose service definition
├── Dockerfile          # Docker image build instructions
├── Makefile            # Convenience commands for build/run/log
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
├── rag/                # Retrieval-Augmented Generation indexer and settings
├── services/           # External service clients (e.g., weather client)
├── tools/              # Tool implementations (shell commands, weather tool, etc.)
├── zzzzzzap.py         # FastAPI app with Signal message handling and routing
```

## Future Work / Roadmap

- Expand the whitelist of safe shell commands
- Enhance RAG capabilities and indexing for broader document types
- Add more tools and integrations to extend assistant functionality
- Improve error handling and logging granularity
- Provide a UI or web dashboard for easier interaction and monitoring
- Support additional messaging platforms beyond Signal

---

This project is designed to be a modular, extensible personal assistant backend leveraging modern AI and messaging technologies.

