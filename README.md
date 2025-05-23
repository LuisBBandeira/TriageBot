# TriageBot

## Overview

TriageBot is an AI-powered virtual triage nurse system built with FastAPI. It leverages Crew AI agents to analyze patient symptoms, assess risk, and provide recommendations. The backend uses PostgreSQL for persistent storage and is fully containerized with Docker and Docker Compose.

## Features

- FastAPI backend with RESTful endpoints
- Crew AI integration for risk assessment
- Modular agent-based architecture
- Persistent storage with PostgreSQL
- Unit and integration tests
- Dockerized deployment

## Crew AI Integration

The `RiskAssessmentAgent` uses Crew AI to analyze structured symptom data and provide risk assessment and likely conditions. The agent is defined in `src/agents/risk_assessment_agent.py` and is invoked via the `/triage/risk-assessment` API endpoint.

## Setup

### Prerequisites

- Docker and Docker Compose installed

### Running the Application

```bash
docker-compose up --build
```

The API will be available at [http://localhost:8000](http://localhost:8000).

### API Documentation

Once running, access Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs).

## Testing

To run all tests:

```bash
docker-compose exec app poetry run pytest
```

## Project Structure

- `src/agents/`: AI agent implementations (Crew AI)
- `src/api/`: FastAPI endpoints
- `src/db/`: Database models and session
- `tests/`: Unit and integration tests

## Brief Report

### What the project does

TriageBot collects patient symptoms, uses Crew AI to assess risk and suggest likely conditions, and routes cases accordingly.

### Implementation challenges

- Integrating Crew AI required refactoring the risk assessment logic.
- Ensuring Dockerized services (API, database, Ollama) communicate correctly.
- Maintaining modular code for testability.

### How challenges were solved

- Used Crew AI's Agent, Task, and Crew abstractions for seamless integration.
- Used Docker Compose for multi-service orchestration.
- Wrote modular agents and comprehensive tests.

## License

MIT
