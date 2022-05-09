from django.contrib import admin

from core.custom_admin import CustomAdmin

from .models import Category, Service


@admin.register(Category)
class CategoryAdmin(CustomAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(CustomAdmin):
    search_fields = ["title"]
