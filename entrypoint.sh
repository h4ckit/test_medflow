#!/bin/sh

echo "Running migrations..."
python manage.py migrate
#python manage.py loaddata initial_data.json
exec "$@"