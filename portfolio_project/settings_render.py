"""
Render-specific settings that override production settings
"""

import os
from .settings_production import *

# Override ALLOWED_HOSTS for Render - force the domain
ALLOWED_HOSTS = [
    'future-fs-01-a6ek.onrender.com',
    '.onrender.com', 
    'localhost',
    '127.0.0.1'
]

# Also try environment variable as backup
render_domain = os.environ.get('ALLOWED_HOSTS', '')
if render_domain:
    ALLOWED_HOSTS.extend(render_domain.split(','))

# Force DEBUG to False for production
DEBUG = False

print(f"ALLOWED_HOSTS set to: {ALLOWED_HOSTS}")
print(f"DEBUG set to: {DEBUG}")
print(f"Settings module: {__name__}")