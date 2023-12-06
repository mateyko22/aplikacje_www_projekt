from rest_framework import permissions
from .models import CustomUser


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.reader == request.user


class IsLibrarianOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return request.user.who_is == CustomUser.WhoIsChoices.LIBRARIAN

        return False


class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.who_is == CustomUser.WhoIsChoices.LIBRARIAN

        return False


class IsOwnerOrLibrarian(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.who_is == 'Librarian':
            return True

        return obj == request.user
