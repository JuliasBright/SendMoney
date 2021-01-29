from django.contrib import admin

# Register your models here.
from .models import Patient_register, Booking_Patient

admin.site.register(Patient_register)

admin.site.register(Booking_Patient)