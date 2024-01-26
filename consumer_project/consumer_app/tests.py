from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import BankTransaction
from unittest.mock import patch, MagicMock

class TransactionListTests(TestCase):
    def setUp(self):
        # Set up an instance of the Django REST framework API client
        self.client = APIClient()

    def test_transaction_list_view(self):
        # Generate the URL for the 'transaction_list' view
        url = reverse('transaction_list')
        # Make a GET request to the 'transaction_list' view
        response = self.client.get(url)

        # Ensure that the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions based on your expected behavior

    def test_transaction_list_view_empty(self):
        # Delete all BankTransaction objects to ensure an empty database
        BankTransaction.objects.all().delete()
        # Generate the URL for the 'transaction_list' view
        url = reverse('transaction_list')
        # Make a GET request to the 'transaction_list' view
        response = self.client.get(url)

        # Ensure that the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ensure that the response contains a specific message for an empty state
        self.assertContains(response, 'No transactions found.')  


class CeleryTaskTests(TestCase):
    @patch('consumer_app.tasks.process_bank_transaction')
    def test_celery_task(self, mock_process_bank_transaction):
        # Mock external dependencies and ensure that the Celery task behaves as expected
        # as example,  mock the processing logic and assert that it's called with the expected arguments
        mock_process_bank_transaction.return_value = {'processed_balance': 200.0, 'processed_date': '2024-01-25T12:00:00'}


class WebhookViewTests(TestCase):
    @patch('consumer_app.tasks.process_bank_transaction')
    def test_webhook_view(self, mock_process_bank_transaction):
        # Mock the Celery task's return value
        mock_process_bank_transaction.return_value = {'processed_balance': 200.0, 'processed_date': '2024-01-25T12:00:00'}

        # Generate the URL for the 'webhook_view' endpoint
        url = reverse('webhook_view')
        # Prepare data for the POST request
        data = {'processed_data': 'some_data', 'transaction_id': 1}
        # Make a POST request to the 'webhook_view' endpoint with the prepared data
        response = self.client.post(url, data=data, format='json')

        # Ensure that the response status code is HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ensure that the response JSON matches the expected success response
        self.assertEqual(response.json(), {'status': 'success'})

