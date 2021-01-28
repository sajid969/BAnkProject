from django.db import models

# Create your models here.

class BankDetails(models.Model):
    ifsc = models.CharField(max_length=30)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=100, blank=True)
    address = models.TextField(max_length=256, blank=True)
    city = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    bank_name = models.CharField(max_length=100, blank=True)
