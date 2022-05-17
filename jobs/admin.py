from django.contrib import admin
from core.custom_admin import CustomAdmin
from .models import Job, Skill


@admin.register(Job)
class JobAdmin(CustomAdmin):
    pass

# @admin.register(State)
# class StateAdmin(CustomAdmin):
#     pass
#
# @admin.register(Country)
# class CountryAdmin(CustomAdmin):
#     pass

# @admin.register(Profile)
# class ProfileAdmin(CustomAdmin):
#     pass

@admin.register(Skill)
class SkillAdmin(CustomAdmin):
    pass
