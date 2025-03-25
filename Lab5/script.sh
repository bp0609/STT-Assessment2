#!/bin/bash

# Base directories
MODULE_DIR="algorithms/$1"
OUTPUT_DIR="testSuiteC"

# Ensure the output directory exists
mkdir -p $OUTPUT_DIR

# Iterate over each Python file in the module directory
find $MODULE_DIR -type f -name "*.py" | while read -r file; do
    # Extract the module name and path
    module_path=$(dirname "$file")
    module_name=$(basename "$file" .py)
    
    # Run Pynguin
    echo "Running Pynguin for module $module_name"
    pynguin --project-path="$module_path" --module-name="$module_name" --output-path="$OUTPUT_DIR" --export-strategy=PY_TEST
done