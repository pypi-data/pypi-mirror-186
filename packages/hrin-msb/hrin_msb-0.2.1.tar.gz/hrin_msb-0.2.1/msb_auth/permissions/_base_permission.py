from rest_framework.permissions import BasePermission


class Permisson(BasePermission):
	def has_permission(self, request, view):
		return True

	def has_object_permission(self, request, view, obj):
		return True


class LoginRequiredPermission(Permisson):

	def has_permission(self, request, view):
		return bool(request.user and request.user.is_authenticated)


class AdminUserPermission(Permisson):
	def has_permission(self, request, view):
		return bool(request.user and request.user.is_staff)
