# Import the AppConfig class from the django.apps module
from django.apps import AppConfig

# Create a configuration class for the 'consumer_app' Django app
class ConsumerAppConfig(AppConfig):
    # Specify the default auto-generated primary key field for models
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Set the name of the Django app to 'consumer_app'
    name = 'consumer_app'

