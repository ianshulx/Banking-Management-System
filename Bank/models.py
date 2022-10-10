from django.db import models

# Create your models here.

class Customer(models.Model):
    acc_no = models.BigIntegerField()
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    balance = models.IntegerField()
    img = models.ImageField()

class Transaction(models.Model):
    debited_from = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sender")
    credited_to = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="receiver")
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default="PENDING")

