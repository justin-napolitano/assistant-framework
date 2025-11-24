---
slug: github-assistant-framework-writing-overview
id: github-assistant-framework-writing-overview
title: Building My Own Signal-Driven Personal Assistant with Assistant Framework
repo: justin-napolitano/assistant-framework
githubUrl: https://github.com/justin-napolitano/assistant-framework
generatedAt: '2025-11-24T17:05:12.789Z'
source: github-auto
summary: >-
  I’ve always wanted a personal assistant that can intelligently handle tasks
  and fetch information for me. That’s why I created the Assistant Framework.
  It’s not just another bot; it's a powerful personal assistant service that
  seamlessly integrates with the Signal messaging app, powered by FastAPI and
  LangChain.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

I’ve always wanted a personal assistant that can intelligently handle tasks and fetch information for me. That’s why I created the Assistant Framework. It’s not just another bot; it's a powerful personal assistant service that seamlessly integrates with the Signal messaging app, powered by FastAPI and LangChain.

## What is Assistant Framework?

The Assistant Framework is a signal-driven personal assistant service. It takes Signal messages and processes them through an array of tools or a large language model (LLM) to execute commands and respond accordingly. Don't think of it as a simple command execution tool; it's designed to be versatile, leveraging AI capabilities to interact with users in a natural way.

## Why Does It Exist?

Honestly, I built this project because I needed a reliable assistant that wouldn’t just perform tasks on demand but could also engage intelligently. There are plenty of chatbots out there, but I wanted one that felt more personal and integrated with my daily life. Plus, who doesn't want a techy way to fetch weather updates or check status on the fly?

## Key Design Decisions

Here’s how I approached the design:

- **Signal Messaging Integration**: I chose to use signal-cli-rest-api for its robust handling of Signal messages. It allows me to receive messages asynchronously, which is crucial for a responsive assistant.
- **Command Handling Using LLMs**: I integrated LangChain along with the OpenAI API for natural language processing. This allows users to type commands like `/ask <question>` and get thoughtful, context-aware answers.
- **Tooling Safety**: Executing shell commands can be risky, especially if not properly managed. I built tooling around safe shell command execution to mitigate potential issues.
- **RAG (Retrieval-Augmented Generation)**: I wanted my assistant to be able to query local document indexes to pull relevant information when needed. That's where RAG comes into play, and I’m excited about the possibilities here.

## Tech Stack

Here’s what I used to build it all:

- **Python 3**: The foundational language, because it’s my go-to for anything API or AI-related.
- **FastAPI**: For building the HTTP API. It’s fast, easy to use, and fits perfectly with async tasks.
- **LangChain and OpenAI API**: For the language model side of things, giving the assistant its conversational abilities.
- **signal-cli-rest-api**: To handle our Signal messaging—clever and effective.
- **HTTPX**: For asynchronous HTTP requests, because performance matters.
- **Docker and Docker Compose**: To make deployment straightforward and consistent.

## Project Structure

To give you an idea of how it’s organized, here’s a simplified view of the project structure:

```
.
├── agent.py            # Core logic for the assistant
├── app.py              # Entry point and orchestration
├── docker-compose.yml  # Service definitions for Docker
├── Dockerfile          # Instructions to build Docker images
├── Makefile            # Easy commands for common tasks
├── README.md           # Docs for getting started
├── requirements.txt    # Dependencies to run the project
├── rag/                # For Retrieval-Augmented Generation
├── services/           # Clients for external services (like weather)
├── tools/              # Different tool implementations
├── zzzzzzap.py         # FastAPI app specifically for Signal handling
```

## Features

This framework packs in some solid features:

- **Asynchronous Handling**: Polls and processes Signal messages without blocking the main thread.
- **Command Support**: Recognizes commands like `/help`, `/status`, `/weather <city>`, and `/run <cmd>`.
- **Enhanced Language Processing**: Integrates advanced NLP capabilities through OpenAI and LangChain.
- **Weather Integration**: Can fetch weather info with a simple command.
- **Optional RAG**: If you want to query your local documents for more accurate context.

## Tradeoffs

Every design choice comes with its pros and cons:

- The complexity of using language models can lead to slower responses compared to simpler command APIs, but the tradeoff is richer interactions.
- Integrating multiple tools to manage command execution means there’s a steeper learning curve if someone wants to contribute or extend it.
- RAG opens up flexibility but requires careful tuning to ensure it retrieves the right information.

## Next Steps

I’m constantly looking for ways to improve. Here’s what’s on my roadmap:

- **Expand Command Whitelist**: I want to allow a broader range of safe shell commands for user flexibility.
- **Enhanced RAG Capabilities**: Broadening the types of documents indexed for better information retrieval is key.
- **More Tools & Integrations**: I’m keen on adding more external services to extend the assistant’s functionality.
- **Error Handling & Logging**: More robust logging and better error messaging are on my radar.
- **User Interface**: A web dashboard or UI would really elevate the user experience.
- **Additional Messaging Platforms**: I’d love to support other messaging platforms beyond just Signal.

## Let’s Stay Connected

If you’re interested in keeping up with updates, you can follow my progress on platforms like Mastodon, Bluesky, or Twitter/X. I often share insights and new features as they roll out.

## Wrapping Up

The Assistant Framework is more than just a project; it’s an ongoing experiment in blending personal productivity with the latest in AI and communication technology. Whether you’re looking to use it directly or just want to see how it evolves, I think you’ll find something useful along the way. Check out the code on [GitHub](https://github.com/justin-napolitano/assistant-framework) and feel free to contribute!
