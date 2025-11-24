---
slug: github-assistant-framework
title: 'assistant-core: Signal-Driven Personal Assistant with FastAPI and LangChain'
repo: justin-napolitano/assistant-framework
githubUrl: https://github.com/justin-napolitano/assistant-framework
generatedAt: '2025-11-23T08:14:45.405223Z'
source: github-auto
summary: >-
  Description of assistant-core, a personal assistant using Signal messages, FastAPI, LangChain, and
  local tools to process commands securely and asynchronously.
tags:
  - fastapi
  - langchain
  - signal-cli
  - personal-assistant
  - async-python
  - docker
seoPrimaryKeyword: assistant-core
seoSecondaryKeywords:
  - signal-cli-rest-api
  - fastapi
  - langchain
  - personal assistant
seoOptimized: true
topicFamily: automation
topicFamilyConfidence: 0.95
topicFamilyNotes: >-
  The post describes building and deploying a personal assistant automation system involving APIs,
  asynchronous python, tool integrations, and docker deployment, matching the 'Automation' family
  which covers automation of build, deployment, scripts, docker, and programming workflows.
---

# Building assistant-core: A Signal-Driven Personal Assistant with FastAPI and LangChain

Hey there! I wanted to share some insights and the story behind my recent project, **assistant-core** — a personal assistant that listens to your Signal messages and responds intelligently using a combination of custom tools and language models.

## Why I Built This

I've always been fascinated by personal assistants and chatbots, but I wanted something that lives entirely under my control, integrates with Signal (my preferred messaging app), and can flexibly run commands or fetch info on demand. Existing assistants often feel heavyweight or cloud-dependent, so I set out to build a lightweight, signal-driven assistant that could run locally or in a containerized environment.

## What Problem Does It Solve?

The core problem is: how to have a personal assistant that you can message via Signal and get automated, context-aware responses — without relying on third-party cloud services for message handling.

This project solves that by:

- Polling messages from `signal-cli-rest-api`, a REST interface for Signal
- Parsing commands sent via Signal messages
- Routing those commands to different "tools" — like fetching weather, running safe shell commands, or querying local documents
- Optionally using OpenAI's language models via LangChain for more conversational or complex queries
- Sending replies back through a notifier gateway

## How It's Built

The backbone is a FastAPI app (`zzzzzzap.py`) that continuously polls Signal messages and processes them asynchronously. It uses environment variables for configuration, including API endpoints, tokens, and feature toggles.

The assistant logic is encapsulated in `agent.py` and `app.py`, where commands are parsed and dispatched. For example, `/weather Orlando` triggers a call to a weather service client, while `/run uptime` executes a whitelisted shell command safely.

I integrated LangChain with OpenAI's ChatOpenAI to enable natural language processing and to optionally augment responses with Retrieval-Augmented Generation (RAG) from local documents stored in a data directory.

The project also includes a small suite of tools:

- `tools/shell.py` for running safe shell commands with a whitelist
- `tools/weather.py` and `tools/weather_tool.py` for fetching weather info
- `services/weather_client.py` for communicating with an external weather microservice

Docker and Docker Compose are used for easy deployment, with a `Makefile` providing handy commands to build, run, and tail logs.

## Interesting Implementation Details

- **Safe Shell Execution**: Instead of blindly running commands, I maintain a whitelist of allowed commands (`uptime`, `df`, `docker-ps`) to avoid security risks.

- **RAG Integration**: The assistant can query local markdown or text documents using a vector store index powered by `llama_index`. This is toggled via `DISABLE_RAG` environment variable.

- **Signal Integration**: The app expects a separate Signal stack running (signal-cli-rest-api and notifier gateway). It handles authorization tokens and allowed senders to control access.

- **Asynchronous HTTP Calls**: Using `httpx.AsyncClient` for sending notifications ensures non-blocking IO.

- **Flexible Command Parsing**: Weather commands accept city and optional state inputs, with fallback defaults.

## Why This Project Matters for My Career

Building assistant-core has been a fantastic learning experience in combining cutting-edge NLP tools with real-world messaging platforms. It pushed me to deepen my understanding of asynchronous Python, API design, containerization, and secure command execution.

Moreover, it showcases my ability to architect modular, extensible systems that integrate multiple services and APIs — a skill highly valuable in today's software landscape.

This project is a solid portfolio piece demonstrating practical application of AI, microservices, and messaging integration, all of which are hot topics in the industry.

---

Thanks for reading! If you want to try it out or contribute, check out the repo and drop me a message on Signal.


