from django.contrib import admin
from core.custom_admin import CustomAdmin
from .models import Job, State


@admin.register(Job)
class JobAdmin(CustomAdmin):
    pass

@admin.register(State)
class StateAdmin(CustomAdmin):
    pass
