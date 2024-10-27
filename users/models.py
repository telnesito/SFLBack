from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UsersDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    country = models.CharField(max_length=256)
    user_role = models.CharField(max_length=10, choices=[('NURSE', 'Nurse'), ('PATIENT', 'Patient')])
    ci = models.CharField(max_length=20)
    
    
