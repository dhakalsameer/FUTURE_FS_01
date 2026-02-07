#!/bin/bash
set -e  # Exit on any error

echo "Starting Django portfolio deployment..."

# Set environment variables
export DJANGO_SETTINGS_MODULE=portfolio_project.settings_render
export ALLOWED_HOSTS=${ALLOWED_HOSTS:-"future-fs-01-a6ek.onrender.com,.onrender.com,localhost,127.0.0.1"}
export DEBUG=${DEBUG:-"False"}

echo "Settings module: $DJANGO_SETTINGS_MODULE"
echo "ALLOWED_HOSTS: $ALLOWED_HOSTS"
echo "DEBUG: $DEBUG"

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput || echo "Migrations failed"

# Check if we have real data to import, otherwise create sample data
if [ -f "portfolio_data.json" ]; then
    echo "Importing real portfolio data..."
    python manage.py import_data || echo "Import failed, trying sample data..."
    python manage.py create_sample_data || echo "Sample data creation also failed"
else
    echo "No real data found, creating sample data..."
    python manage.py create_sample_data || echo "Sample data creation failed"
fi

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput || echo "Static files collection failed"

# Start the application
echo "Starting gunicorn on port $PORT..."
exec gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120