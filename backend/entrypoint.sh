#!/bin/bash

# Use PORT environment variable if set, otherwise default to 8000
PORT=${PORT:-8000}

# Run gunicorn with the specified port
exec gunicorn \
    --bind "0.0.0.0:${PORT}" \
    --workers 4 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    config.wsgi:application

