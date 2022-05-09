from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages["duplicate_username"])


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = [
        "username",
        "is_active",
        "is_staff",
        "is_customer",
        "is_worker",
        "is_superuser",
    ]
    list_filter = [
        "is_customer",
        "is_worker",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (
            "More Info",
            {"fields": ("is_customer", "is_worker", "photo")},
        ),
    )


admin.site.register(User, MyUserAdmin)
