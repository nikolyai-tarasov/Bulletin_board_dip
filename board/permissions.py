from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    """ Класс пермишен для определения прав Менеджера """
    def has_permission(self, request, view):
        if request.user.groups.filter(name="Manager").exists():
            return True
        return False


class IsOwner(BasePermission):
    """ Класс пермишен для определения прав Владельца """
    def has_object_permission(self, request, view, object):
        if object.author == request.user:
            return True
        return False
