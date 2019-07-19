from django.shortcuts import render
from jobs_api.models import Job
from rest_framework.permissions import AllowAny
from jobs_api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework import viewsets
from jobs_api.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'list' or self.action == 'retrieve' or self.action :
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'destroy' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]

        # if self.action in ('list', 'create', 'retrieve', 'update', 'partial_update', 'destroy'):
        #     permission_classes = [IsAdminUser]
        # elif self.action in

        return [permission() for permission in permission_classes]


