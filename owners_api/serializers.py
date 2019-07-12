from rest_framework import serializers
from owners_api.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('salon_name', 'salon_address', 'salon_city',
                  'salon_state', 'salon_zip', 'salon_phone_number',
                  'salon_description')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name',
                  'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.salon_name = profile_data.get(
            'salon_name', profile.salon_name)
        profile.salon_address = profile_data.get(
            'salon_address', profile.salon_address)
        profile.salon_city = profile_data.get(
            'salon_city', profile.salon_city)
        profile.salon_state = profile_data.get(
            'salon_state', profile.salon_state)
        profile.salon_zip = profile_data.get(
            'salon_zip', profile.salon_zip)
        profile.salon_phone_number = profile_data.get(
            'salon_phone_number', profile.salon_phone_number)
        profile.salon_description = profile_data.get(
            'salon_description', profile.salon_description)
        profile.save()
        return instance





