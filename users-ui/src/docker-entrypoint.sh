#!/bin/sh

gunicorn --workers 2 \
-b 0.0.0.0:5000 \
users-ui:app
