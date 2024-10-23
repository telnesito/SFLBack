from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=200)
    email= models.EmailField()
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
