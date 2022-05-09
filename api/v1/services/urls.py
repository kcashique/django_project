from django.urls import path
from rest_framework.generics import ListAPIView, RetrieveAPIView

from services.models import Category, Service

from .serializers import CategorySerializer, ServiceSerializer, CategorySingleSerializer

app_name = "services"

urlpatterns = [
    path("categories/", ListAPIView.as_view(queryset=Category.objects.filter(is_active=True), serializer_class=CategorySerializer)),
    path("categories/<str:pk>/", RetrieveAPIView.as_view(queryset=Category.objects.filter(is_active=True), serializer_class=CategorySingleSerializer)),
    path("", ListAPIView.as_view(queryset=Service.objects.filter(is_active=True), serializer_class=ServiceSerializer)),
    path("<str:pk>/", RetrieveAPIView.as_view(queryset=Service.objects.filter(is_active=True), serializer_class=ServiceSerializer)),

]
