#!/bin/bash

# Run Arthur strategy simulation
DURATION=100
OUTPUT_DIR="output"
STRATEGY="naive"

python main.py \
    --duration "$DURATION" \
    --output_dir "$OUTPUT_DIR" \
    --strategy "$STRATEGY" "$@"