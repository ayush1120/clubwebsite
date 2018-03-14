from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    component_request = models


class ComponentRequest(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
