from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 允许GET、HEAD、OPTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj == request.user:
            print("Permission granted for user:", request.user,obj)
            return True
        else:
            print("Permission denied for user:", request.user,obj)

        return False

class IsAddressPermissions(permissions.BasePermission):
    """
    自定义权限，只允许对象的所有者访问它，或者只允许对象的所有者编辑它。
    """

    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求，
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        # 只有该snippet的所有者才允许写权限。
        return obj.user == request.user