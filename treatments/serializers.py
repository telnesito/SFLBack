from rest_framework import serializers
from .models import Treatment, MedicineTreatment, HealingTreatment, DailyTreatment

class TreatmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treatment
        fields = '__all__'

class MedicineTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineTreatment
        fields = ['dosis', 'presentation', 'unit']  # NO incluyas 'id_treatment'
        
class HealingTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealingTreatment
        fields = ['video', 'image']  # NO incluyas 'id_treatment'


class DailyTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTreatment
        fields = '__all__'