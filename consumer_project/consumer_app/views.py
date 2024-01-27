# Import necessary modules and classes
from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

# Define a view function to retrieve and display a list of transactions
def transaction_list(request):
     # Define the API URL for transactions
    api_url = 'http://localhost:8000/api/transactions/' 

     # Make a GET request to the transactions API
    response = requests.get(api_url) 

    # Check if the response is successful (HTTP 200 OK)
    if response.status_code == 200:  
        # Parse the JSON response to get transaction data
        transactions = response.json()  
    else:
         # If not successful, set transactions to an empty list
        transactions = [] 
        
    # Render the 'bank_transaction_list.html' template with the retrieved transactions
    return render(request, 'consumer_app/bank_transaction_list.html', {'transactions': transactions})

# Define a view function to submit a new transaction
def submit_transaction(request):
    if request.method == 'POST':  # Check if the request method is POST
        # Extract form data from the POST request
        account_number = request.POST.get('account_number')
        transaction_amount = request.POST.get('transaction_amount')

        # Send the extracted data to the producer app's 'submit_transaction' API endpoint
        producer_api_url = 'http://producer-app/api/submit_transaction/'
        data = {'account_number': account_number, 'transaction_amount': transaction_amount}
        response = requests.post(producer_api_url, json=data)  # Make a POST request with JSON data

        if response.status_code == 200:  # Check if the response is successful (HTTP 200 OK)
            return JsonResponse({'status': 'success'})  # Return a success JSON response
        else:
            return JsonResponse({'status': 'error'})  # Return an error JSON response if not successful

