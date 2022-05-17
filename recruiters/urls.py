from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "recruiters"

urlpatterns = [
    path('recruiters/', login_required(views.RecruiterListView.as_view()),name='recruiter_list'),
    path('recruiters/new/', login_required(views.RecruiterCreateView.as_view()),name='recruiter_new'),
    path('recruiters/<str:pk>/', login_required(views.RecruiterDetailView.as_view()),name='recruiter_detail'),
    path('recruiters/update/<str:pk>/', login_required(views.RecruiterUpdateView.as_view()),name='recruiter_update'),
    path('recruiters/delete/<str:pk>/', login_required(views.RecruiterDeleteView.as_view()),name='recruiter_delete'),

        ]
