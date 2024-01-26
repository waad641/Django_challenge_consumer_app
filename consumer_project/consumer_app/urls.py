# Import the 'path' function from the 'django.urls' module
from django.urls import path

# Import the 'transaction_list' view function from the current app's 'views' module
from .views import transaction_list,submit_transaction

# Define the URL patterns for the app
urlpatterns = [
    path('transactions/', transaction_list, name='transaction_list'),
    path('submit_transaction/', submit_transaction, name='submit_transaction'),
   
]


