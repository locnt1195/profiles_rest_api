from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        import traceback
        traceback.print_stack()
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id