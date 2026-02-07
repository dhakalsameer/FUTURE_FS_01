#!/bin/bash
export DJANGO_SETTINGS_MODULE=portfolio_project.settings_render
export ALLOWED_HOSTS=future-fs-01-a6ek.onrender.com,.onrender.com,localhost,127.0.0.1
python manage.py migrate --noinput

# Check if we have real data to import, otherwise create sample data
if [ -f "portfolio_data.json" ]; then
    echo "Importing real portfolio data..."
    python manage.py import_data
else
    echo "No real data found, creating sample data..."
    python manage.py create_sample_data
fi

python manage.py collectstatic --noinput
gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:$PORT