from django.contrib import admin
from core.custom_admin import CustomAdmin
from .models import Applicant, JobApplication

# Register your models here.
@admin.register(JobApplication)
class JobApplication(CustomAdmin):
    pass

@admin.register(Applicant)
class ApplicantAdmin(CustomAdmin):
    pass
