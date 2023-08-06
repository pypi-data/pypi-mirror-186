from os import environ
from ._endpoint import ApiEndpoint


class ApiHost:
	_app_name: str = 'app'
	_host_url: str = ''
	_auth_token: str = ''
	_endpoint: str = ''

	def __str__(self):
		return f"<{self.__class__.__name__} {self._app_name.upper()} at '{self._host_url}' >"

	def __init__(self, **kwargs):
		self._app_name = kwargs.get('app_name')
		self._host_url = kwargs.get('host_url')
		self._auth_token = kwargs.get('auth_token')

		if self._app_name not in ['', None] and self._host_url in ['', None]:
			self._host_url = environ.get(f'{self._app_name.upper()}_HOST_URL', default='').rstrip('/')

		if self._auth_token not in ['', None] and self._app_name != '':
			self._auth_token = environ.get(f'{self._app_name.upper()}_ACCESS_TOKEN', default='')

	@property
	def host_url(self):
		return f"{self._host_url.rstrip('/')}/{self._app_name}"

	@property
	def endpoint(self):
		return f"/{self._endpoint.rstrip('/').replace('.', '/')}" if self._endpoint else ''

	@property
	def request_url(self):
		return f"{self.host_url}/<api_version>{self.endpoint}"

	def create_endpoint(self, method: str = None, endpoint: str = None, **kwargs) -> ApiEndpoint:
		self._endpoint = endpoint
		return ApiEndpoint(
			url=self.request_url, method=method,
			**{**kwargs, 'auth_token': self._auth_token, 'version_text': "<api_version>"}
		)

	def api_get(self, endpoint: str = None, **kwargs) -> ApiEndpoint:
		return self.create_endpoint(method='GET', endpoint=endpoint, **kwargs)

	def api_put(self, endpoint: str = None, **kwargs) -> ApiEndpoint:
		return self.create_endpoint(method='PUT', endpoint=endpoint, **kwargs)

	def api_post(self, endpoint: str = None, **kwargs) -> ApiEndpoint:
		return self.create_endpoint(method='POST', endpoint=endpoint, **kwargs)

	def api_delete(self, endpoint: str = None, **kwargs) -> ApiEndpoint:
		return self.create_endpoint(method='DELETE', endpoint=endpoint, **kwargs)
