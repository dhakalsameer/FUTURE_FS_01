#!/bin/bash
export DJANGO_SETTINGS_MODULE=portfolio_project.settings_render
export ALLOWED_HOSTS=future-fs-01-a6ek.onrender.com,.onrender.com,localhost,127.0.0.1
python manage.py migrate --noinput
python manage.py create_sample_data
python manage.py collectstatic --noinput
gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:$PORT