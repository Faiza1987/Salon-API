from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=10)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    salon_name = models.CharField(max_length=20)
    salon_address = models.CharField(max_length=255)
    salon_city = models.CharField(max_length=255)
    salon_state = models.CharField(max_length=2)
    salon_zip = models.CharField(max_length=5)
    salon_phone_number = models.CharField(max_length=10)
    salon_description = models.TextField(max_length=2000)
