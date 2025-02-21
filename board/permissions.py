from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Manager").exists():
            return True
        return False


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, object):
        if object.author == request.user:
            return True
        return False