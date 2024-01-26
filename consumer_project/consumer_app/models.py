# consumer_app/models.py
from django.db import models

class BankTransaction(models.Model):
    account_number = models.CharField(max_length=20)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    processed_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Transaction {self.id}"

