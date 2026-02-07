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
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Fix media files for Render
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Serve media files in production (needed for Render)
if not DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add better error handling
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# Logging for debugging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'portfolio': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

print(f"ALLOWED_HOSTS set to: {ALLOWED_HOSTS}")
print(f"DEBUG set to: {DEBUG}")
print(f"Settings module: {__name__}")
print(f"MEDIA_URL: {MEDIA_URL}")
print(f"MEDIA_ROOT: {MEDIA_ROOT}")
print(f"Database config: {DATABASES['default']['ENGINE']}")
print(f"Database name: {DATABASES['default'].get('NAME', 'N/A')}")