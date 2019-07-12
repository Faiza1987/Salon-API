from rest_framework import viewsets
from owners_api.models import User
from owners_api.serializers import UserSerializer
from rest_framework.permissions import AllowAny
from owners_api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from owners_api.models import User, UserProfile


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list' or self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' \
                or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        return [permission() for permission in permission_classes]
