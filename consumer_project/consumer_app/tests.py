# Import necessary modules and classes for testing
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import BankTransaction
from unittest.mock import patch, MagicMock

# Define a test case class for testing the 'TransactionList' view
class TransactionListTests(TestCase):
    def setUp(self):
        # Set up an instance of the Django REST framework API client
        self.client = APIClient()

    # Test the behavior of the 'transaction_list' view
    def test_transaction_list_view(self):
        # Generate the URL for the 'transaction_list' view
        url = reverse('transaction_list') 
        # Make a GET request to the 'transaction_list' view
        response = self.client.get(url)  

        # Ensure a successful response
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        

    # Test the behavior of the 'transaction_list' view when the database is empty
    def test_transaction_list_view_empty(self):
        
         # Delete all BankTransaction objects
        BankTransaction.objects.all().delete()

        # Generate the URL for the 'transaction_list' view
        url = reverse('transaction_list')  

         # Make a GET request to the 'transaction_list' view
        response = self.client.get(url) 

         # Ensure a successful response
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

         # Ensure a specific message for an empty state
        self.assertContains(response, 'No transactions found.') 
        
# Define a test case class for testing Celery tasks
class CeleryTaskTests(TestCase):
    @patch('consumer_app.tasks.process_bank_transaction')
    def test_celery_task(self, mock_process_bank_transaction):
        mock_process_bank_transaction.return_value = {'processed_balance': 200.0, 'processed_date': '2024-01-25T12:00:00'}
        # Mock external dependencies and assert Celery task behavior

# Define a test case class for testing the 'webhook_view' endpoint
class WebhookViewTests(TestCase):
    @patch('consumer_app.tasks.process_bank_transaction')
    def test_webhook_view(self, mock_process_bank_transaction):
        mock_process_bank_transaction.return_value = {'processed_balance': 200.0, 'processed_date': '2024-01-25T12:00:00'}
        url = reverse('webhook_view')  # Generate the URL for the 'webhook_view' endpoint
        
        # Prepare data for the POST request
        data = {'processed_data': 'some_data', 'transaction_id': 1}  
        
         # Make a POST request to the 'webhook_view' endpoint
        response = self.client.post(url, data=data, format='json') 
        
         # Ensure a successful response
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        
         # Ensure the expected success response
        self.assertEqual(response.json(), {'status': 'success'}) 
