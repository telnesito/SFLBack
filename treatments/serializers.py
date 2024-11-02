from rest_framework import serializers
from .models import Treatment, MedicineTreatment, HealingTreatment, DailyTreatment

class TreatmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treatment
        fields = '__all__'

class MedicineTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineTreatment
        fields = '__all__'

class HealingTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealingTreatment
        fields = '__all__'


class DailyTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTreatment
        fields = '__all__'