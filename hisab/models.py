from django.db import models

class Khata(models.Model):
    customer_name = models.CharField(max_length=100)
    reason = models.CharField(max_length=200)
    amount = models.IntegerField()
    TRANSACTION_TYPE = [
        ('INCOME', 'Income'),
        ('EXPENSE', 'Expense'),
    ]
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.amount}"