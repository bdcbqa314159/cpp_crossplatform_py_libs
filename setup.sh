#!/bin/bash

# =========== setup paths =========== #
export LD_LIBRARY_PATH=$(pwd)/build/bin:$LD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$(pwd)/build/bin:$DYLD_LIBRARY_PATH

# =========== setup python environment =========== #
source .venv/bin/activate

echo "Environment set up successfully."

# =========== building python package =========== #
echo "Building the python package..."

cd python
python3 -m pip install .
cd ..
echo "Python package built successfully."

# =========== testing the python package =========== #
echo ""
echo "==========================="
echo "Testing python application..."
echo ""

cd apps
python3 testing.py