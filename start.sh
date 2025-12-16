#!/bin/bash

# Path to your virtual environment
VENV_PATH="./.venv"

# Path to your Python script
SCRIPT_PATH="./wolForwarder.py"

# Activate the virtual environment and run the script in the background using nohup
nohup "$VENV_PATH/bin/python" "$SCRIPT_PATH" > output.log 2>&1 &

# Print the process ID (optional)
echo "Python script is running in the background with PID $!"
