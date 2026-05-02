#!/bin/bash

# Exit immediately if a command fails
set -e

# Navigate to project directory (optional, adjust if needed)
cd "$(dirname "$0")"

# Activate virtual environment
source ubuvenv/bin/activate

# Run the Python script
python3 main.py
