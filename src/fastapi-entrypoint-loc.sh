#!/bin/sh
echo "Waiting for postgres..."
while ! nc -z base_db 5432; do
  sleep 0.5
done
echo "PostgreSQL started"
sleep 0.5
uvicorn main:app --reload --host 0.0.0.0 --port 9000
exec "$@"
