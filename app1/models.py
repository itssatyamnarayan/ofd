from django.db import models

# Create your models here.
class CustomerRegister(models.Model):
    user_name=models.CharField(max_length=25)
    email=models.EmailField()
    password=models.CharField(max_length=15)
