from rest_framework import viewsets
from api.models import User
from api.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create' or self.action == 'list':
            permission_classes = [AllowAny]

        elif self.action == 'retreive' or self.action == 'update' \
                or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]

        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]