#!/bin/bash

echo "Running tests..."

pytest

if [ $? -eq 0 ]; then
    echo "All tests PASSED! Initializing API..."
    ngrok http 8000 --log=stdout > /dev/null &
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
else
    echo "Tests FAILED! The container will not be started."
    exit 1
fi