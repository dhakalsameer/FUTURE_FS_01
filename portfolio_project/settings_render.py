"""
Render-specific settings that override production settings
"""

import os
from .settings_production import *

# Override ALLOWED_HOSTS for Render
render_domain = os.environ.get('ALLOWED_HOSTS', '')
if render_domain:
    ALLOWED_HOSTS = render_domain.split(',')
else:
    # Fallback to explicit domain
    ALLOWED_HOSTS = [
        'future-fs-01-a6ek.onrender.com',
        '.onrender.com',
        'localhost',
        '127.0.0.1'
    ]

print(f"ALLOWED_HOSTS set to: {ALLOWED_HOSTS}")