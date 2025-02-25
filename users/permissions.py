from rest_framework.permissions import BasePermission


class IsUserOwner(BasePermission):
    """ Класс пермишен для определения прав Владельца """
    def has_object_permission(self, request, view, obj):
        return request.user == obj
