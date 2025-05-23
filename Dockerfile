FROM python:3.11-slim

# Install system dependencies (venv, build tools, git)
RUN apt-get update && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install -n

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
