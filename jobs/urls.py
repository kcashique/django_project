from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "jobs"

urlpatterns = [
    path('jobs/', login_required(views.JobListView.as_view()),name='job_list'),
    path('jobs/new/', login_required(views.JobCreateView.as_view()),name='job_new'),
    path('jobs/<str:pk>/', login_required(views.JobDetailView.as_view()),name='job_detail'),
    path('jobs/update/<str:pk>/', login_required(views.JobUpdateView.as_view()),name='job_update'),
    path('jobs/delete/<str:pk>/', login_required(views.JobDeleteView.as_view()),name='job_delete'),
]
