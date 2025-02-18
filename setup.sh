#!/bin/bash

echo "Setting up the environment..."

# Define the environment directory
ENV_DIR="venv"

# Create the virtual environment
echo "Creating virtual environment..."
python3 -m venv $ENV_DIR

# Activate the virtual environment
source $ENV_DIR/bin/activate

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Finished environment setup."
