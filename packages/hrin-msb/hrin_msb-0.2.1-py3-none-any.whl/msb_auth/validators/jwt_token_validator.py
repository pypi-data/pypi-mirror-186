from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from msb_auth.users import TokenUser
from msb_cipher import Cipher
from msb_http import RequestWrapper


class JwtTokenValidator(JWTTokenUserAuthentication):
	"""
	This class overrides the "JWTTokenUserAuthentication", so that we can implement
	custom authentication rules over the default system

	"""

	_request: RequestWrapper = None

	def __validate_token_owner(self, token: TokenUser = None):
		return f"{self._request.user_agent}@{self._request.ip}" == token.owner

	def __validate_token_integrity(self, token: TokenUser = None) -> bool:
		return token.is_authenticated and self.__validate_token_owner(token=token)

	def authenticate(self, request):
		try:
			self._request = RequestWrapper(request=request)
			auth_result = super(JWTTokenUserAuthentication, self).authenticate(request=request)
			if auth_result:
				token_user: TokenUser = auth_result[0]
				token_user.set_validation_status(self.__validate_token_integrity(token=token_user))
			return auth_result
		except Exception as e:
			return None
