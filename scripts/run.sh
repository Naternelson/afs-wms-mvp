#!/bin/bash

echo "🚀 Starting FastAPI server..."

# Check if venv exists before activating
scripts/activate.sh

# Start FastAPI
uvicorn src.backend.main:app --host 0.0.0.0 --port 8000 --reload
