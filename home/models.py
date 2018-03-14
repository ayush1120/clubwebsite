from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    component_request = models


class Component(models.Model):
    ComponentName = models.CharField(max_length=20)

    def __str__(self):
        return self.ComponentName


class ComponentRequest(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    mobileno = models.BigIntegerField()
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
