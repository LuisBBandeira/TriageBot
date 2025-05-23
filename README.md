# TriageBot

## Project Overview
TriageBot is a FastAPI-based application designed to assist with symptom intake, risk assessment, and case routing. It leverages modern Python libraries and tools to provide a robust and scalable solution.

## Project Structure
```bash
triagebot/
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── README.md
├── virtual_triage.db
├── scripts/
│   ├── ollama-entrypoint.sh
│   ├── test_llm.py
├── src/
│   ├── __init__.py
│   ├── llm.py
│   ├── logging_config.py
│   ├── main.py
│   ├── utils.py
│   ├── agents/
│   │   ├── agent_utils.py
│   │   ├── risk_assessment_agent.py
│   │   ├── routing_agent.py
│   │   ├── symptom_intake_agent.py
│   ├── api/
│   │   ├── dependencies.py
│   │   ├── endpoints/
│   │   │   ├── auth.py
│   │   │   ├── triage.py
│   ├── auth/
│   │   ├── security.py
│   ├── db/
│   │   ├── models.py
│   │   ├── session.py
├── tests/
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_api.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_agents.py
```

## Code Structure
- **Agents**: Implements core logic for symptom intake, risk assessment, and case routing.
  - `SymptomIntakeAgent`: Collects symptoms from raw input.
  - `RiskAssessmentAgent`: Assesses risk based on symptoms.
  - `RoutingAgent`: Routes cases based on risk data.
- **API**: Provides endpoints for interacting with the agents.
- **Auth**: Handles user authentication and security, including password hashing and JWT-based token generation.
- **Database**: Defines ORM models for `User`, `Patient`, and `TriageCase`.

## Test Coverage
- **Unit Tests**: Covers individual agent functionalities (`test_agents.py`).
- **Integration Tests**: Validates API endpoints for symptom intake, risk assessment, and case routing (`test_api.py`).

## Security Controls
- Passwords are hashed using bcrypt.
- JWT-based authentication is implemented with token expiration.
- **Risks**:
  - Hardcoded secret key should be replaced with an environment variable.
  - Mock database should be replaced with a production-ready database.

## Documentation Completeness
The documentation provides:
- Project overview and structure.
- Setup instructions.
- Example API usage.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd TriageBot
   ```

2. **Install Dependencies**:
   - Using Poetry:
     ```bash
     poetry install
     ```

3. **Run the Application**:
   - Using Docker Compose:
     ```bash
     docker-compose up --build
     ```

4. **Run Tests**:
   - Execute all tests using pytest:
     ```bash
     pytest
     ```

5. **Access the Application**:
   - The application will be available at `http://localhost:8000`.

## Example cURL Commands
1. **Symptom Intake**:
   ```bash
   curl -X POST http://localhost:8000/triage/symptom-intake \
   -H "Content-Type: application/json" \
   'http://localhost:8000/triage/symptom-intake?raw_input=I%20have%20a%20headache%20and%20nausea' \
   -d ''
   ```

2. **Risk Assessment**:
   ```bash
   curl -X 'POST' \
  'http://localhost:8000/triage/risk-assessment' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"symptoms": {"fever": true, "cough": true}}'
   ```

3. **Route Case**:
   ```bash
   curl -X 'POST' \
  'http://localhost:8000/triage/route-case' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"risk_data": {"risk_level": "high"}}'
   ```
