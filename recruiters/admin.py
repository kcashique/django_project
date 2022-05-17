from django.contrib import admin
from core.custom_admin import CustomAdmin
from .models import Recruiter


@admin.register(Recruiter)
class Recruiter(CustomAdmin):
    pass
