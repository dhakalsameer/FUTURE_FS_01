FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for Pillow
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Make start script executable
RUN chmod +x start.sh

RUN python manage.py collectstatic --noinput

EXPOSE $PORT

CMD bash start.sh