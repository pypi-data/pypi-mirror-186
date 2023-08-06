from ._client import ApiRequestClient


class ApiEndpoint():
	__version_text = ''
	_url: str = ''
	_method: str = 'GET'

	def __str__(self):
		return f"<{self.__class__.__name__} {self._method.upper()} '{self._url}'>"

	def __init__(self, url: str = None, method: str = None, **kwargs):
		if kwargs.get('version_text'):
			self.__version_text = kwargs.get('version_text')
		self._url = url.rstrip('/')
		self._method = method

		self._init_data = kwargs

	def __versioned_api_request(self, version=1) -> ApiRequestClient:
		self._url = self._url.replace(self.__version_text, f'v{version}')
		return ApiRequestClient(url=self._url, method=self._method, **self._init_data)

	@property
	def v1(self) -> ApiRequestClient:
		return self.__versioned_api_request(version=1)

	@property
	def v2(self) -> ApiRequestClient:
		return self.__versioned_api_request(version=2)
