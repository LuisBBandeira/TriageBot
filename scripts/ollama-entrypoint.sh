#!/bin/sh
set -e

# Install wget if not present
if ! command -v wget > /dev/null 2>&1; then
  if command -v apk > /dev/null 2>&1; then
    apk add --no-cache wget
  elif command -v apt-get > /dev/null 2>&1; then
    apt-get update && apt-get install -y wget
  fi
fi

# Start Ollama server in the background
/usr/bin/ollama serve &
OLLAMA_PID=$!

# Wait for Ollama server to be ready using wget
until wget -qO- http://localhost:11434/api/tags > /dev/null 2>&1; do
  echo "Waiting for Ollama server to be ready..."
  sleep 2
done

# Pull the required model
ollama pull tinyllama

# Bring Ollama server to foreground (wait on it)
wait $OLLAMA_PID
