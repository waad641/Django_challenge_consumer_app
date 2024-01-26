# Importing necessary features to ensure compatibility and smooth transition to Python 3
from __future__ import absolute_import, unicode_literals

# Import the 'os' module to interact with the operating system
import os

# Import the 'Celery' class from the 'celery' module
from celery import Celery

# Set the default Django settings module for the Celery application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consumer_project.settings')

# Create an instance of the Celery class named 'celery_app' for the consumer project
celery_app = Celery('consumer_project')

# Configure the Celery app to use the Django settings
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Set the message broker URL for RabbitMQ
celery_app.conf.broker_url = 'pyamqp://guest:guest@localhost:5672//'

# Set the result backend to use Django Celery Results
celery_app.conf.result_backend = 'django-db'

# Discover and automatically register tasks in the 'tasks.py' modules of Django apps
celery_app.autodiscover_tasks()
