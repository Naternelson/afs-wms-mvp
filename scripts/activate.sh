#!/bin/bash
# Check if venv exists before activating
if [ -d "venv" ]; then
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate  # Linux/Mac
    elif [ -f "venv/Scripts/activate" ]; then
        source venv/Scripts/activate  # Windows Git Bash
    else
        echo "❌ Error: Virtual environment activation script not found!"
        exit 1
    fi
else
    echo "❌ Error: Virtual environment does not exist. Run 'scripts/setup.sh' first."
    exit 1
fi
echo "Python VE running"