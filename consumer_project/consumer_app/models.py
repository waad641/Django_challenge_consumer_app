# Import the models module from Django
from django.db import models

# Create a Django model named 'BankTransaction'
class BankTransaction(models.Model):
    # Define a character field for the account number with a maximum length of 20 characters
    account_number = models.CharField(max_length=20)

    # Define a decimal field for the transaction amount with a maximum of 10 digits and 2 decimal places
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Define a date and time field for the transaction date, automatically set to the current date and time when created
    transaction_date = models.DateTimeField(auto_now_add=True)

    # Define a JSON field for storing processed data, allowing it to be blank or null
    processed_data = models.JSONField(blank=True, null=True)

    # Define a string representation for the model
    def __str__(self):
        # Return a formatted string indicating the transaction ID
        return f"Transaction {self.id}"


