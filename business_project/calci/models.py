from django.db import models
from datetime import datetime

# Create your models here.
class Ledger(models.Model):
    seller_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    items = models.CharField(max_length=100)
    bill_amount = models.DecimalField(max_digits=100,decimal_places=2)
    received_amount = models.DecimalField(max_digits=100,decimal_places=2)
    balance_amount = models.DecimalField(max_digits=100,decimal_places=2)
    profit = models.DecimalField(max_digits=100,decimal_places=2)

    created_date_time = models.DateTimeField(auto_now_add= True, blank = True)
    updated_date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.customer_name + " purchased items worth of "+ str(self.bill_amount)
