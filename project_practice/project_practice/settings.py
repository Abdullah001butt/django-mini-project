import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Use environment variable for secret key in production
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-8_3gtg+1i+pw6xqwj%0o0x2t9+f3@#it$g@*q6$6ag4yxdl+f$')

# Set DEBUG based on environment
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Add your deployment URLs
ALLOWED_HOSTS = ['.vercel.app', '.now.sh', 'localhost', '127.0.0.1']

# Your existing INSTALLED_APPS

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    # ... your existing middleware
]

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files configuration
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Keep your existing configurations for:
# - TEMPLATES
# - AUTH_PASSWORD_VALIDATORS
# - LANGUAGE_CODE
# - TIME_ZONE
# - USE_I18N
# - USE_TZ
# - DEFAULT_AUTO_FIELD

# Remove NPM_BIN_PATH for production
