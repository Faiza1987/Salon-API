from django.urls import path, include
from rest_framework import routers
from jobs_api.views import JobViewSet

router = routers.DefaultRouter()
router.register('jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]