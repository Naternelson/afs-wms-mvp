#!/bin/bash

echo "🔧 Setting up the project..."

# Create and activate virtual environment
scripts/activate.sh

echo "✅ Activating virtual environment..."
source venv/Scripts/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Ensure required directories exist
mkdir -p src/backend/api/v1/routes src/backend/core src/backend/models src/backend/schemas src/backend/services tests

echo "✅ Setup complete! Run 'source venv/bin/activate' to activate the virtual environment."
