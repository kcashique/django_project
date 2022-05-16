from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path("", login_required(views.Index.as_view()), name="index"),

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

    path('districts/', login_required(views.DistrictListView.as_view()),name='district_list'),
    path('districts/new/', login_required(views.DistrictCreateView.as_view()),name='district_new'),
    path('districts/<str:pk>/', login_required(views.DistrictDetailView.as_view()),name='district_detail'),
    path('districts/update/<str:pk>/', login_required(views.DistrictUpdateView.as_view()),name='district_update'),
    path('districts/delete/<str:pk>/', login_required(views.DistrictDeleteView.as_view()),name='district_delete'),

]
