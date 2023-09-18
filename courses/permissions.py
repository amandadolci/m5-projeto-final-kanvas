from rest_framework import permissions


class SuperUserOrGetPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_authenticated and (
            request.user.is_superuser or request.method == "GET"
        )


class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_authenticated and request.user.is_superuser
