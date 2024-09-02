from django.contrib import admin

# Register your models here.

from .models.user_models import Users 

admin.site.register(Users)
