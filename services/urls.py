from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('services/', login_required(views.ServiceListView.as_view()),name='service_list'),
    path('services/new/', login_required(views.ServiceCreateView.as_view()),name='service_new'),
    path('services/<str:pk>/', login_required(views.ServiceDetailView.as_view()),name='service_detail'),
    path('services/update/<str:pk>/', login_required(views.ServiceUpdateView.as_view()),name='service_update'),
    path('services/delete/<str:pk>/', login_required(views.ServiceDeleteView.as_view()),name='service_delete'),

    path('categories/', login_required(views.CategoryListView.as_view()),name='category_list'),
    path('categorys/new/', login_required(views.CategoryCreateView.as_view()),name='category_new'),
    path('categorys/<str:pk>/', login_required(views.CategoryDetailView.as_view()),name='category_detail'),
    path('categorys/update/<str:pk>/', login_required(views.CategoryUpdateView.as_view()),name='category_update'),
    path('categorys/delete/<str:pk>/', login_required(views.CategoryDeleteView.as_view()),name='category_delete'),


]
