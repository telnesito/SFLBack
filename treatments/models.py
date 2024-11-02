from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Treatment(models.Model):
  id_treatment = models.AutoField(primary_key=True)
  id_user = models.ForeignKey(User, on_delete=models.CASCADE) 
  nombre = models.CharField(max_length=100)
  start_date = models.DateField()
  end_date = models.DateField()
  hours = models.IntegerField()
  comment = models.CharField(max_length=100)
  treatments_type = models.CharField(max_length=10, choices=[('MEDICINE', 'Medicine'),('HEALINGS','Healings')])
 
class MedicineTreatment(models.Model):
    id_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, parent_link=True)
    dosis = models.CharField(max_length=50)
    presentation = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)

    
class HealingTreatment(models.Model):
    id_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, parent_link=True)
    video = models.FileField(upload_to='healings/')
    image = models.FileField(upload_to='healings/')
    

class DailyTreatment(models.Model):
    id_treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name='daily_treatments')
    date = models.DateField()
    taken = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)