#!/bin/bash

echo "🔧 Setting up the project..."

# Create and activate virtual environment
scripts/activate.sh

echo "✅ Activating virtual environment..."
source venv/Scripts/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt
pip freeze > requirements.txt

echo "✅ Setup complete! Run 'source venv/bin/activate' to activate the virtual environment."
