#!/bin/bash

# PythonAnywhere Deployment Script
# This script helps deploy updates to your Django portfolio

echo "🚀 Starting PythonAnywhere deployment..."

# Check if we're on PythonAnywhere
if [[ ! -d "/home" ]]; then
    echo "❌ This script must be run on PythonAnywhere"
    exit 1
fi

# Get current directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "📁 Current directory: $(pwd)"

# Activate virtual environment (update path as needed)
if [[ -d "/home/$USER/.virtualenvs/portfolioenv" ]]; then
    source /home/$USER/.virtualenvs/portfolioenv/bin/activate
    echo "✅ Virtual environment activated"
else
    echo "⚠️  Virtual environment not found. Please create it first."
    echo "   Run: mkvirtualenv --python=/usr/bin/python3.10 portfolioenv"
    exit 1
fi

# Install/update dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput --settings=portfolio_project.settings_production

# Run migrations
echo "🗄️  Running database migrations..."
python manage.py migrate --settings=portfolio_project.settings_production

# Restart the web app
echo "🔄 Restarting web app..."
touch /var/www/www_yourusername_pythonanywhere_com_wsgi.py 2>/dev/null || echo "⚠️  Could not restart web app automatically"

echo "✅ Deployment completed!"
echo "🌐 Your site should be available at: https://yourusername.pythonanywhere.com"
echo ""
echo "📝 Next steps:"
echo "   1. Update your username in the WSGI file"
echo "   2. Check the web app in PythonAnywhere dashboard"
echo "   3. Test your site functionality"