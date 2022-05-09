from django.contrib import admin

from .custom_admin import CustomAdmin
from .models import Area


@admin.register(Area)
class AreaAdmin(CustomAdmin):
    pass
