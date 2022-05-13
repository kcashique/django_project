from django.contrib import admin
from core.custom_admin import CustomAdmin
from .models import Job, Country, State


@admin.register(Job)
class JobAdmin(CustomAdmin):
    pass

@admin.register(Country)
class CountryAdmin(CustomAdmin):
    pass

@admin.register(State)
class StateAdmin(CustomAdmin):
    pass
