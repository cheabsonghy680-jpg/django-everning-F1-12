from django.contrib import admin  # type: ignore
from .models import patient

# Register your models here.
admin.site.register(patient)
