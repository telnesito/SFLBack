from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import TreatmentsSerializer, DailyTreatmentSerializer, MedicineTreatmentSerializer, HealingTreatmentSerializer
from .models import DailyTreatment
from rest_framework.response import Response
from django.utils import timezone

@api_view(['POST'])
def create_treatment(req):
    serializer = TreatmentsSerializer(data=req.data)
    medicine_serializer = MedicineTreatmentSerializer(data=req.data)
    healing_serializer = HealingTreatmentSerializer(data=req.data)

    
    # Valida el tratamiento
    if serializer.is_valid():
        # Guarda el tratamiento y obtiene la instancia creada
        treatment = serializer.save()

        # Valida y guarda dependiendo del tipo de tratamiento
        if treatment.treatments_type == 'MEDICINE':
            if medicine_serializer.is_valid():
                medicine_serializer.save(id_treatment=treatment)
            else:
                return Response({"medicine_errors": medicine_serializer.errors})

        elif treatment.treatments_type == 'HEALINGS':
            if healing_serializer.is_valid():
                healing_serializer.save(id_treatment=treatment)
            else:
                return Response({"healing_errors": healing_serializer.errors})
        
        #Hacer esto una funcion
        # Calcula el rango de fechas
        start_date = treatment.start_date
        end_date = treatment.end_date

        # Crea DailyTreatments por cada día en el rango
        current_date = start_date
        while current_date <= end_date:
            DailyTreatment.objects.create(
                id_treatment=treatment,
                date=current_date
            )
            current_date += timezone.timedelta(days=1)  # Avanza un día

        # Filtra los daily_treatments después de crear
        daily_treatments = DailyTreatment.objects.filter(id_treatment=treatment)

        return Response({
            "treatment": serializer.data,
            "medicine": medicine_serializer.data if medicine_serializer.is_valid() else None,
            "healing": healing_serializer.data if healing_serializer.is_valid() else None,
            'daily_treatments': DailyTreatmentSerializer(daily_treatments, many=True).data
        })

    return Response({
        "treatment_errors": serializer.errors
    })

# @transaction.atomic()
# @api_view(['POST'])
# def register(request):
#     serializer = UserSerializer(data=request.data)
#     detailsSerializer = UserDetailsSerializer(data=request.data)
#     if(serializer.is_valid() & detailsSerializer.is_valid()):
#         # Se agrega el registro a la base de datos
#         serializer.save()
        
#         # Buscamos el usuario y le asignamos la clave
#         user = User.objects.get(username=serializer.data['username'])
#         user.set_password(serializer.data['password'])
#         user.save()
        
#         # Le asignamos el user al modelo detailsUser
#         detailsSerializer.save(user=user)
        
#         # Token de registro
#         token = Token.objects.create(user=user)

#         return Response({
#             'token':token.key, 
#             'user':serializer.data,
#             'details':detailsSerializer.data
#         }, 
#         status=status.HTTP_201_CREATED)
#     return Response({
#         'user':serializer.errors,
#         'details':detailsSerializer.errors
#         },status=status.HTTP_400_BAD_REQUEST)
