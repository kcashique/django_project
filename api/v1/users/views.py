from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User
from . import serializers


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = serializers.UserTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer


class ProfileView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ProfileSerializer

    def get_object(self):
        return self.request.user


class UpdateProfileView(UpdateAPIView):
    serializer_class = serializers.UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class AccountUpdateView(UpdateAPIView):
    model = User
    serializer_class = serializers.AccountUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.first_name = serializer.data.get("first_name")
            self.object.last_name = serializer.data.get("last_name")
            self.object.save()
            response = {
                "status": True,
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdatePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UpdatePasswordSerializer

    def get_object(self):
        return self.request.user


class UpdatePhotoView(UpdateAPIView):
    serializer_class = serializers.UpdatePhotoSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
