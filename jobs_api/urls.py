from django.urls import path, include
from rest_framework import routers
from jobs_api.views import JobViewSet
from jobs_api.views import LoggedInUserJobList

router = routers.DefaultRouter()
router.register('jobs', JobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jobs/myjobs', LoggedInUserJobList.as_view())
]