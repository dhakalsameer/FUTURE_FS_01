import os
import sys
from dotenv import load_dotenv

# Add your project directory to the Python path
project_home = '/home/sameer07/FUTURE_FS_01'  # Your PythonAnywhere username
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings_production')

# Load environment variables
load_dotenv(os.path.join(project_home, '.env'))

# Activate the virtual environment
activate_this = '/home/sameer07/.virtualenvs/portfolioenv/bin/activate'  # Your virtualenv path
exec(open(activate_this).read(), {'__file__': activate_this})

# Import Django
import django
django.setup()

# Import your WSGI application
from portfolio_project.wsgi import application

# Set the application variable
application = application