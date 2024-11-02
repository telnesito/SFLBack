from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import TreatmentsSerializer, DailyTreatmentSerializer, MedicineTreatmentSerializer, HealingTreatmentSerializer
from rest_framework.response import Response
from django.db import transaction
from .services.create_daily_treatments import create_daily_treatments
from .services.handle_treatment import handle_treatment
from rest_framework import status

serializers_map = {
    'MEDICINE': MedicineTreatmentSerializer,
    'HEALINGS': HealingTreatmentSerializer
    }

@api_view(['POST'])
@transaction.atomic
def create_treatment(req):
        
    serializer = TreatmentsSerializer(data=req.data)

    if serializer.is_valid():
        treatment = serializer.save()
        # Response data es un obj donde se construye la respuesta del metodo
        response_data = {
            "treatment": serializer.data,
            "daily_treatments": []
        }

        #Creamos los daily_treatments en base al treatments
        daily_treatments = create_daily_treatments(treatment)
        # Lo agregamos a response data
        response_data['daily_treatments'] = DailyTreatmentSerializer(daily_treatments, many=True).data
        
        #Obtenemos el treatment_type que mando el usuario
        treatment_type = treatment.treatments_type
        # Obtenemos el treatment.type de map
        treatment_type_serializer = serializers_map.get(treatment_type)
        # Si el usuario mando un treatment.type valido, entonces agregamos los demas campos al response
        if treatment_type_serializer:
            return handle_treatment(req, treatment, response_data, treatment_type_serializer)
              

    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

