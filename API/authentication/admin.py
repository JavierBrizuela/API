from django.contrib import admin
from django.contrib.auth.models import Group
from authentication.models import CustomUser

admin.site.unregister(Group)
admin.site.register(CustomUser)