from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path("", login_required(views.Index.as_view()), name="index"),
]
