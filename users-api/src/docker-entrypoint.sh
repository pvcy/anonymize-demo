#!/bin/sh

if [ "$LOAD_DATA" = "True" ]; then
  echo "Loading Data..."
  python load-data.py
else
  echo "Skipping data loading"
fi

gunicorn --workers 2 \
-b 0.0.0.0:8000 \
users-api:app
