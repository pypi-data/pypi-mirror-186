from ._auth_token import AuthToken
from ._datastructures import (
	UserPermissions, UserName, UserRole, UserCountry, UserImage, UserLocation, UserRegisteredApp,
	UserAccountType
)


class TokenUser(AuthToken):

	@property
	def number(self):
		return self._get("employee_number")

	@property
	def name(self) -> UserName:
		return UserName(
			first=self._get("first_name"), middle=self._get("middle_name"),
			last=self._get("last_name"), full=self._get("full_name")
		)

	@property
	def image(self) -> UserImage:
		return self._get("image")



	@property
	def work_id(self):
		return self._get("work_id")

	@property
	def role(self) -> UserRole:
		return UserRole(**self._get('role', default={}))

	@property
	def country(self) -> UserCountry:
		return UserCountry(**self._get('country', default={}))

	@property
	def account_type(self) -> UserAccountType:
		return UserAccountType(id=self._get("account_type_id"), name=self._get("account_type_name"))

	@property
	def permission(self) -> list[UserPermissions]:
		return list[UserPermissions()]

	@property
	def registered_apps(self) -> list[UserRegisteredApp]:
		return [UserRegisteredApp(id=app.get("id"), name=app.get("name")) for app in self._get("registered_apps")]
