from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_customer"] = user.is_customer
        token["is_worker"] = user.is_worker
        token["is_supervisor"] = user.is_supervisor
        token["is_staff"] = user.is_staff
        token["is_superuser"] = user.is_superuser
        return token

    def validate(cls, attrs):
        data = super(MyTokenObtainPairSerializer, cls).validate(attrs)
        refresh = cls.get_token(cls.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["is_customer"] = bool(cls.user.is_customer)
        data["is_worker"] = bool(cls.user.is_worker)
        data["is_supervisor"] = bool(cls.user.is_supervisor)
        data["is_staff"] = bool(cls.user.is_staff)
        data["is_superuser"] = bool(cls.user.is_superuser)
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
