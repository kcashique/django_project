from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(UserTokenObtainPairSerializer, cls).get_token(user)
        return token

    def validate(cls, attrs):
        data = super(UserTokenObtainPairSerializer, cls).validate(attrs)
        refresh = cls.get_token(cls.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["is_customer"] = bool(cls.user.is_customer)
        data["is_worker"] = bool(cls.user.is_worker)
        data["is_supervisor"] = bool(cls.user.is_supervisor)
        data["is_staff"] = bool(cls.user.is_staff)
        data["is_superuser"] = bool(cls.user.is_superuser)
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["user_permissions", "password","groups"]


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "password2",
            "first_name",
            "last_name",
            "email",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user



class UpdatePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("photo",)


class AccountUpdateSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)


class UpdatePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )
        return value

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user.pk != instance.pk:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission for this user."}
            )
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
