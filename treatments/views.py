from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import TreatmentsSerializer, DailyTreatmentSerializer, MedicineTreatmentSerializer, HealingTreatmentSerializer
from rest_framework.response import Response
from django.db import transaction
from .services.create_daily_treatments import create_daily_treatments
from .services.handle_treatment import handle_treatment
from rest_framework import status
from .models import Treatment, HealingTreatment,MedicineTreatment,DailyTreatment

serializers_map = {
    'MEDICINE': MedicineTreatmentSerializer,
    'HEALINGS': HealingTreatmentSerializer
    }
@api_view(['POST'])
@transaction.atomic
def create_treatment(req):
    serializer = TreatmentsSerializer(data=req.data)

    if serializer.is_valid():
        # 1. Guardamos el tratamiento en la base de datos
        treatment = serializer.save()

        # 2. Creamos los daily_treatments en base al treatment
        daily_treatments = create_daily_treatments(treatment)
        response_data = {
            "treatment": serializer.data,
            "daily_treatments": DailyTreatmentSerializer(daily_treatments, many=True).data
        }

        # 3. Procesamos el tratamiento específico basado en el tipo
        treatment_type = treatment.treatments_type
        treatment_type_serializer = serializers_map.get(treatment_type)

        if treatment_type_serializer:
            # Ahora llamamos a handle_treatment y le pasamos el tratamiento creado
            return handle_treatment(req, treatment, response_data, treatment_type_serializer)

    # Si hay errores de validación, retornamos un error 400
    return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# todo: Enviar los modulos a otros archivos
def get_daily_treatments(treatment):
    return list(treatment.daily_treatments.all().values('date', 'taken', 'notes'))

# refactorizar
def get_medicine_treatment(treatment):
    medicine_treatment = MedicineTreatment.objects.filter(id_treatment=treatment).values('dosis', 'presentation', 'unit').first()
    return medicine_treatment if medicine_treatment else {}

def get_healing_treatment(treatment):
    healing_treatment = HealingTreatment.objects.filter(id_treatment=treatment).values('video', 'image').first()
    return healing_treatment if healing_treatment else {}

@api_view(['GET'])
def get_user_treatments(request, user_id):
    # Filtrar tratamientos solo por el usuario especificado
    treatments = Treatment.objects.prefetch_related('daily_treatments').filter(id_user=user_id)
    
    treatments_data = []
    
    for treatment in treatments:
        treatment_data = {
            'id_user': treatment.id_user.pk,
            'id_treatment': treatment.id_treatment,
            'nombre': treatment.nombre,
            'start_date': treatment.start_date,
            'end_date': treatment.end_date,
            'hours': treatment.hours,
            'comment': treatment.comment,
            'treatments_type': treatment.treatments_type,
            'daily_treatments': get_daily_treatments(treatment),
        }
        # Agregar campo específico según el tipo de tratamiento
        if treatment.treatments_type == 'MEDICINE':
            treatment_data['medicine_treatment'] = get_medicine_treatment(treatment)
        elif treatment.treatments_type == 'HEALINGS':
            treatment_data['healing_treatment'] = get_healing_treatment(treatment)
        
        treatments_data.append(treatment_data)

    return Response({'treatments': treatments_data}, status=status.HTTP_200_OK)

# to do: Hacer que la URL vaya el id
@api_view(['POST'])
def get_treatment(request):
    treatment_id = request.data.get('id_treatment')
    
    if not treatment_id:
        return Response({'error': 'El id_treatment es requerido'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Obtener el tratamiento específico
        treatment = Treatment.objects.prefetch_related('daily_treatments').get(id_treatment=treatment_id)
    except Treatment.DoesNotExist:
        return Response({'error': 'Tratamiento no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    # Construir el diccionario con los datos del tratamiento
    treatment_data = {
        'id_user': treatment.id_user.pk,
        'id_treatment': treatment.id_treatment,
        'nombre': treatment.nombre,
        'start_date': treatment.start_date,
        'end_date': treatment.end_date,
        'hours': treatment.hours,
        'comment': treatment.comment,
        'treatments_type': treatment.treatments_type,
        'daily_treatments': get_daily_treatments(treatment),
    }
    
    # Agregar campo específico según el tipo de tratamiento
    if treatment.treatments_type == 'MEDICINE':
        treatment_data['medicine_treatment'] = get_medicine_treatment(treatment)
    elif treatment.treatments_type == 'HEALINGS':
        treatment_data['healing_treatment'] = get_healing_treatment(treatment)
    
    return Response({'treatment': treatment_data}, status=status.HTTP_200_OK)
