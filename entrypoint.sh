#!/bin/sh

echo "Running migrations..."
python manage.py migrate
echo "Creating admin..."
python manage.py initadmin
#python manage.py loaddata initial_data.json
exec "$@"