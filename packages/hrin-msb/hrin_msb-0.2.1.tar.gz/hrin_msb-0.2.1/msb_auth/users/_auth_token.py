from django.utils.functional import cached_property
from .._constants import TokenConst
from msb_cipher import Cipher


class AuthToken:
	token: dict
	_username_field: str = TokenConst.username_field
	_userid_field: str = TokenConst.userid_field
	_user_email_field: str = TokenConst.user_email_field

	def __init__(self, tokendata: dict = None):
		self.token = tokendata if tokendata else dict()

	def __str__(self):
		return f"<{self.__class__.__name__} [{self.id}]: {self.email}>"

	def __hash__(self):
		return hash(self.username)

	def __getattr__(self, attr):
		"""This acts as a backup attribute getter for custom claims defined in Token serializers."""
		return self.token.get(attr, None)

	def set_validation_status(self, status: bool = False):
		self.token['is_valid'] = status

	def _get(self, key: str = '', default=None):
		val = self.payload.get(key)
		return val if val is not None else default

	@cached_property
	def payload(self):
		return self.token.get('payload') or {}

	@property
	def owner(self):
		return Cipher.decrypt(self.token.get('owner'))

	@cached_property
	def id(self):
		return self._get(self._userid_field)

	@cached_property
	def userid(self):
		return self.id

	@cached_property
	def username(self):
		return self._get(self._username_field)

	@property
	def email(self):
		return self._get(self._user_email_field)

	@cached_property
	def auth_type(self):
		return self._get('auth_type')

	@cached_property
	def is_admin(self):
		return self._get("is_admin") == True

	@property
	def is_valid(self):
		return self.token.get('is_valid', False)

	@property
	def is_authenticated(self):
		return self._get('is_authenticated', False) and self.is_valid
