

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Doctor, Patient


admin.site.register(UserProfile)

admin.site.register(Doctor)
admin.site.register(Patient)