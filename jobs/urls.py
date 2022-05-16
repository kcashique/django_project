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

    path('countries/', login_required(views.CountryListView.as_view()),name='country_list'),
    path('countries/new/', login_required(views.CountryCreateView.as_view()),name='country_new'),
    path('countries/<str:pk>/', login_required(views.CountryDetailView.as_view()),name='country_detail'),
    path('countries/update/<str:pk>/', login_required(views.CountryUpdateView.as_view()),name='country_update'),
    path('countries/delete/<str:pk>/', login_required(views.CountryDeleteView.as_view()),name='country_delete'),

    path('states/', login_required(views.StateListView.as_view()),name='state_list'),
    path('states/new/', login_required(views.StateCreateView.as_view()),name='state_new'),
    path('states/<str:pk>/', login_required(views.StateDetailView.as_view()),name='state_detail'),
    path('states/update/<str:pk>/', login_required(views.StateUpdateView.as_view()),name='state_update'),
    path('states/delete/<str:pk>/', login_required(views.StateDeleteView.as_view()),name='state_delete'),

    path('companies/', login_required(views.CompanyListView.as_view()),name='company_list'),
    path('companies/new/', login_required(views.CompanyCreateView.as_view()),name='company_new'),
    path('companies/<str:pk>/', login_required(views.CompanyDetailView.as_view()),name='company_detail'),
    path('companies/update/<str:pk>/', login_required(views.CompanyUpdateView.as_view()),name='company_update'),
    path('companies/delete/<str:pk>/', login_required(views.CompanyDeleteView.as_view()),name='company_delete'),
]
