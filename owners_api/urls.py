from django.urls import path, include
from rest_framework import routers
from owners_api.views import UserViewSet
from jobs_api.views import OwnerJobList

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('users/<pk>/jobs', OwnerJobList.as_view())
]
