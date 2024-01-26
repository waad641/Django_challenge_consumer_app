#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Set the Django settings module to 'consumer_project.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consumer_project.settings')
    
    try:
        # Attempt to import the execute_from_command_line function from Django's core management module
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle the case where Django is not installed
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute Django's command-line utility with the provided command-line arguments
    execute_from_command_line(sys.argv)

# Check if the script is being executed directly
if __name__ == '__main__':
    # Call the main function when the script is executed
    main()
