from rest_framework import permissions


# class IsLoggedInUserOrAdmin(permissions.IsAuthenticated):
#     def has_object_permission(self, request, view, obj):
#         return obj == request.job or request.user.is_staff


# class IsAdminUser(permissions.IsAuthenticated):
#     def has_permission(self, request, view):
#         return request.user and request.user.is_staff
#
#     def has_object_permission(self, request, view, obj):
#         return request.user and request.user.is_staff
