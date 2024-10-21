#!/bin/sh
while ! nc -z db 5432; do
  echo "Waiting for database to be ready..."
  sleep 1
done
echo "Database is up and running."

