from rest_framework import permissions

class IsPatientOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user or request.method in permissions.SAFE_METHODS

class IsDoctorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.doctor == request.user or request.method in permissions.SAFE_METHODS
