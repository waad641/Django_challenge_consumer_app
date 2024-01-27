# Overview:
The Consumer App is responsible for receiving bank transaction data from the Producer App,
processing it asynchronously using Celery, and updating the database with the processed results.
It communicates with the Producer App through API calls.

# Components:

   # Tasks:

_process_bank_transaction:_ Asynchronous Celery task that processes bank transaction data and updates the database.
Views:

_webhook_receiver:_ Django REST Framework view that handles incoming POST requests from the Producer App and triggers the Celery task.
Models:

_BankTransaction:_ Django model representing bank transactions with fields like account number, transaction amount, transaction date, and processed data.

 # API Endpoints:

    /api/webhook_receiver/: 'POST' endpoint for receiving transaction data from the Producer App.
    
  # Tests:

Unit tests for views and Celery tasks are available in tests.py.
  # Settings:

Celery is configured in tasks.py.
RabbitMQ is configured in settings.py
# Usage:
on a teminal :
   1/create a virtual environment :
   
     python -m venv venv_consumer
    
  2/Activate the virtual environment :
  
     venv\Scripts\activate  //// if on Unix or MacOS : source venv/bin/activate
    
 3/Install dependencies :
 
     pip install Django Celery requests django-celery-results

     (or you can proceed with installing each dependency alone : pip insatll Djanggo   / pip install celery ... ) 
   
 4/create Django project and application :
 
    django-admin startproject consumer_project
   
 5/locate to the created project :
 
    cd consumer_project 
   
 6/ open the code on vscode :
 
    . code 
    
# RabbitMQ donloading :

before downloadingt rabbitMQ , 
just make sure you have successfully installed Erlang/OTP from   https://www.erlang.org/downloads
after configuring Erlang/OTP (run the .exe file ) you can inastall the RabbitMQ 
from  https://www.rabbitmq.com/download.html
  to make sure rabbitMQ is installed successfuly , open rabbitMQ Server -start and run this command:

    rabbitmqctl status
    
# Run migrations : 
    python manage.py makemigrations 
    python manage.py migrate
    
# Start Django development server: 
    python manage.py runserver

# Run Celery worker: 

    celery -A consumer_project worker -l info
  
# Start Django development server: 

    python manage.py runserver

# versions:
   python : 3.11.5,
   
   django : 5.0.1,
   
   celery : 5.3.6,
   
   rabbitMQ : 3.12.12.0,
   
   Erlang/OTP : 26.2.1.0
