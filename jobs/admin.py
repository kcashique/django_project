from django.contrib import admin
from core.custom_admin import CustomAdmin
from .models import Job, Location


@admin.register(Job)
class JobAdmin(CustomAdmin):
    pass

    @admin.register(Location)
    class LocationAdmin(CustomAdmin):
        pass
