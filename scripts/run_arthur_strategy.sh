#!/bin/bash

# Run Arthur strategy simulation
DURATION=100
OUTPUT_DIR="output"
STRATEGY="arthur"


SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${SCRIPT_DIR}/.."
PYTHON_SCRIPT="${PROJECT_ROOT}/main.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: $PYTHON_SCRIPT not found."
    exit 1
fi

python3 "$PYTHON_SCRIPT" \
    --duration "$DURATION" \
    --output_dir "$OUTPUT_DIR" \
    --strategy "$STRATEGY" "$@"