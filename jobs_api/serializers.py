from rest_framework import serializers
from jobs_api.models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ("title", "hourly_rate", "company", "address", "city", "state", "zip_code",
                  "description", "contact_email", "owner")