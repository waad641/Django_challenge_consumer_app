# Django_challenge_consumer_app
This repository focus on the :
# Consumer App :

# Overview:
The Consumer App is responsible for receiving bank transaction data from the Producer App, processing it asynchronously using Celery, and updating the database with the processed results. It communicates with the Producer App through API calls.



Web Server:

Manages incoming HTTP requests.
Exposes endpoints for users to view and submit transactions.
Django Application:

Contains views to render HTML pages for users.
Sends requests to the Producer App to submit transactions.
Celery Worker:

Asynchronously processes submitted transactions.
Calls the Producer App's webhook with processed data.
Communication Flow:

User interacts with the Consumer App's web interface.
Consumer App sends transaction data to the Producer App for storage.
Producer App stores the transaction in the database and initiates asynchronous processing.
Celery worker in the Consumer App processes the transaction asynchronously.
Once processing is complete, the Celery worker in the Consumer App sends processed data to the Producer App's webhook.
Producer App updates the transaction in the database with the processed data.
External Services:

Celery Broker (RabbitMQ or similar):
Manages the message queue for Celery tasks.
Database Server:
Hosts the databases for both Consumer and Producer Apps.




