from django.contrib import admin
from home.models import Component, ComponentRequest, UserProfileInfo

# Register your models here.
admin.site.register(Component)
admin.site.register(ComponentRequest)
admin.site.register(UserProfileInfo)
