# Import the 'shared_task' decorator from the 'celery' module
from celery import shared_task

# Import the 'requests' module for making HTTP requests
import requests

# Import the 'BankTransaction' model and 'AsyncResult' class from the '.models' module
from .models import BankTransaction
from celery.result import AsyncResult

# Decorate a function as a shared Celery task
@shared_task
def process_bank_transaction(transaction_id, account_number, transaction_amount):
    # Perform some processing on the data (asynchronously)
    processed_data = {
        'processed_balance': transaction_amount * 2,  # Placeholder logic
        'processed_date': '2024-01-24T12:00:00',  # Placeholder timestamp
    }

    # Update the 'BankTransaction' model with the processed data
    transaction = BankTransaction.objects.get(id=transaction_id)
    transaction.processed_data = processed_data
    transaction.save()

    # Send the result back to the producer's webhook URL
    webhook_url = "http://producer_app/api/webhook_receiver/" 
    requests.post(webhook_url, json={
        'transaction_id': transaction_id,
        'processed_data': processed_data,
    })

    # Return the processed data as the result of the Celery task
    return processed_data
