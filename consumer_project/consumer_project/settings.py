# Import the 'Path' class from the 'pathlib' module
from pathlib import Path

# Build paths inside the project using 'Path'. Resolve the absolute path of the project's parent directory.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings which is not recommended for production
# for a better setting we can See : https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# Security warning: Keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mx$mz1ca4jy0=7m#$ihg6wh()kt8@uh@y3f96xy2@em5$ra&0c'

# Security warning: Don't run with debug turned on in production!
DEBUG = False

# Define the allowed hosts for the consumer application
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'consumer_app',
    'django_celery_results',
    'celery',
]

# Middleware classes to process requests and responses globally
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration for the project
ROOT_URLCONF = 'consumer_project.urls'

# Configuration for template rendering
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application entry point
WSGI_APPLICATION = 'consumer_project.wsgi.application'

# django Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation configuration
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuration for serving static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery configuration for the consumer project
# RabbitMQ broker URL
CELERY_BROKER_URL = 'pyamqp://guest:guest@localhost:5672//' 

# Use Django Celery Results as the result backend
CELERY_RESULT_BACKEND = 'django-db'  
