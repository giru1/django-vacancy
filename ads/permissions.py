from rest_framework.permissions import BasePermission


class AdsPermission(BasePermission):
    message = "You don't have permission 1"

    def has_object_permission(self, request, view, obj):
        return obj.author.id == request.user.id or request.user.role in ['moderator', 'admin']


