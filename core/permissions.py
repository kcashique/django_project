from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated


class GenericAPIException(APIException):
    """
    raises API exceptions with custom messages and custom status codes
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "error"

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code


class IsOwner(IsAuthenticated):
    """Custom permission to only allow owners of an object to edit it."""

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class IsAdminUser(IsAuthenticated):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff
