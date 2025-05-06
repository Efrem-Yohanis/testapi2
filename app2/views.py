from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Custom GET to return users with profiles
    @action(detail=True, methods=['get'])
    def profiles(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    # PUT is already handled by ModelViewSet (which includes PUT, PATCH, DELETE)
