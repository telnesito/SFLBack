from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, UserDetailsSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.db import transaction
from .models import UsersDetails

@api_view(['POST'])
def login(request):
    
    user = get_object_or_404(User, username=request.data['username'])
    
    
    if not user.check_password(request.data['password']):
        return Response({
            "error":"Invalid password"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance = user)
    
    return Response({
            'token':token.key, 
            'user':serializer.data,
        }, status=status.HTTP_200_OK)

@transaction.atomic()
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    detailsSerializer = UserDetailsSerializer(data=request.data)
    if(serializer.is_valid() & detailsSerializer.is_valid()):
        # Se agrega el registro a la base de datos
        serializer.save()
        
        # Buscamos el usuario y le asignamos la clave
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        
        # Le asignamos el user al modelo detailsUser
        detailsSerializer.save(user=user)
        
        # Token de registro
        token = Token.objects.create(user=user)

        return Response({
            'token':token.key, 
            'user':serializer.data,
            'details':detailsSerializer.data
        }, 
        status=status.HTTP_201_CREATED)
    return Response({
        'user':serializer.errors,
        'details':detailsSerializer.errors
        },status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request): 
    user = User.objects.select_related('usersdetails').get(pk=request.user.pk) 
    
    details = user.usersdetails
    details_serializer = UserDetailsSerializer(instance=details)
 
    return Response({'user': UserSerializer(instance=user).data, 'details': [details_serializer.data],}, status=status.HTTP_200_OK)

