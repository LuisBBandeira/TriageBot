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

4. **Access the Application**:
   - The application will be available at `http://localhost:8000`.

## Example cURL Commands
1. **Symptom Intake**:
   ```bash
   curl -X POST http://localhost:8000/triage/symptom-intake \
   -H "Content-Type: application/json" \
   -d '{"raw_input": "I have a fever and cough."}'
   ```

2. **Risk Assessment**:
   ```bash
   curl -X POST http://localhost:8000/risk-assessment \
   -H "Content-Type: application/json" \
   -d '{"symptoms": {"fever": true, "cough": true}}'
   ```

3. **Route Case**:
   ```bash
   curl -X POST http://localhost:8000/route-case \
   -H "Content-Type: application/json" \
   -d '{"risk_data": {"risk_level": "high"}}'
   ```

4. **Login**:
   ```bash
   curl -X POST http://localhost:8000/login \
   -H "Content-Type: application/x-www-form-urlencoded" \
   -d "username=your_username&password=your_password"
