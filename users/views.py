from .models import Users
from rest_framework import permissions, viewsets

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('created_at')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

