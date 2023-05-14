from django.contrib import admin
from .models import Entries as Profile,Files

# Register your models here.

admin.site.register(Profile)
admin.site.register(Files)