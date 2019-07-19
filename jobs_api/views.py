from django.shortcuts import render
from jobs_api.models import Job
from rest_framework.permissions import AllowAny
from jobs_api.permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework import viewsets
from jobs_api.serializers import JobSerializer
from rest_framework import generics


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        permission_classes = []

        if self.action == 'list' or self.action == 'retrieve' or self.action == 'create' or \
                self.action == 'partial_update' or self.action == 'update':
            permission_classes = [IsLoggedInUserOrAdmin]

        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class LoggedInUserJobList(generics.ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        return Job.objects.filter(owner=self.request.user)


