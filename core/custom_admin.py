from import_export.admin import ImportExportModelAdmin

from .actions import mark_active, mark_inactive


class CustomAdmin(ImportExportModelAdmin):
    exclude = ["creator"]
    list_display = ("__str__", "created", "updated", "is_active")
    list_filter = ("is_active",)
    actions = [mark_active, mark_inactive]

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)
