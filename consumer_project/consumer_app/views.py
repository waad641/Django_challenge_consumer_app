from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

def transaction_list(request):
    api_url = 'http://localhost:8000/api/transactions/'
    response = requests.get(api_url)

    if response.status_code == 200:
        transactions = response.json()
    else:
        transactions = []

    return render(request, 'consumer_app/bank_transaction_list.html', {'transactions': transactions})

def submit_transaction(request):
    if request.method == 'POST':
        # Extract form data
        account_number = request.POST.get('account_number')
        transaction_amount = request.POST.get('transaction_amount')

        # Send data to producer app
        producer_api_url = 'http://producer-app/api/submit_transaction/'
        data = {'account_number': account_number, 'transaction_amount': transaction_amount}
        response = requests.post(producer_api_url, json=data)

        if response.status_code == 200:
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})

