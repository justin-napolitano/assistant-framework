---
slug: github-assistant-framework-note-technical-overview
id: github-assistant-framework-note-technical-overview
title: Assistant Framework Overview
repo: justin-napolitano/assistant-framework
githubUrl: https://github.com/justin-napolitano/assistant-framework
generatedAt: '2025-11-24T18:30:57.676Z'
source: github-auto
summary: >-
  The Assistant Framework is a signal-driven personal assistant built on FastAPI
  and LangChain. It listens for Signal messages via the signal-cli-rest-api,
  processes commands, and responds through a notifier gateway.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

The Assistant Framework is a signal-driven personal assistant built on FastAPI and LangChain. It listens for Signal messages via the signal-cli-rest-api, processes commands, and responds through a notifier gateway.

## Key Features

- Asynchronous polling of Signal messages
- Commands: `/help`, `/status`, `/weather [city]`, `/run <cmd>`, `/ask <question>`
- LangChain and OpenAI API integration for powerful language processing
- Safe execution of shell commands and weather info retrieval
- Retrieval-Augmented Generation (RAG) for local document queries
- Fully containerized with Docker and Docker Compose

## Getting Started

### Prerequisites

- Docker & Docker Compose installed
- Signal stack configured
- OpenAI API key (optional)

### Quick Run

1. Copy and configure the environment file:

   ```bash
   cp .env.example .env
   # Edit .env for details
   ```

2. Start the service:

   ```bash
   make run
   ```

3. Check logs:

   ```bash
   make logs
   ```

**Gotcha:** Make sure you've set up your Signal environment variables correctly.
