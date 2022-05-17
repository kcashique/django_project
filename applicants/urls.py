from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "applicants"

urlpatterns = [
    path('applicants/', login_required(views.ApplicantListView.as_view()),name='applicant_list'),
    path('applicants/new/', login_required(views.ApplicantCreateView.as_view()),name='applicant_new'),
    path('applicants/<str:pk>/', login_required(views.ApplicantDetailView.as_view()),name='applicant_detail'),
    path('applicants/update/<str:pk>/', login_required(views.ApplicantUpdateView.as_view()),name='applicant_update'),
    path('applicants/delete/<str:pk>/', login_required(views.ApplicantDeleteView.as_view()),name='applicant_delete'),

    path('applicants/', login_required(views.JobApplicationListView.as_view()),name='jobapplication_list'),
    path('applicants/new/', login_required(views.JobApplicationCreateView.as_view()),name='jobapplicion_new'),
    path('applicants/<str:pk>/', login_required(views.JobApplicationDetailView.as_view()),name='jobapplicantion_detail'),
    path('applicants/update/<str:pk>/', login_required(views.JobApplicationUpdateView.as_view()),name='jobapplicantion_update'),
    path('applicants/delete/<str:pk>/', login_required(views.JobApplicationDeleteView.as_view()),name='jobapplicantion_delete'),

    ]
