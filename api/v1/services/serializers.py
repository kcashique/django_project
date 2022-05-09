from rest_framework import serializers

from services.models import Category, Service


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class CategorySingleSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(source="get_services", many=True)

    class Meta:
        model = Category
        fields = "__all__"
