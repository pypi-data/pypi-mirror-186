

class ApiRequestClient:
	_url: str = ''
	__headers: dict = dict()
	_request_method: str = 'GET'

	def get(self, data: dict = None, url_params: dict = None, **opt):
		self.__set_request_url(url=opt.get('endpoint'), params=url_params)
		return self.__make_request(method='GET', data=data, **opt)

	def post(self, data: dict = None, url_params: dict = None, **opt):
		self.__set_request_url(url=opt.get('endpoint'), params=url_params)
		return self.__make_request(method='POST', data=data, **opt)

	def put(self, data: dict = None, url_params: dict = None, **opt):
		self.__set_request_url(url=opt.get('endpoint'), params=url_params)
		return self.__make_request(method='PUT', data=data, **opt)

	def delete(self, data: dict = None, url_params: dict = None, **opt):
		self.__set_request_url(url=opt.get('endpoint'), params=url_params)
		return self.__make_request(method='DELETE', data=data, **opt)

	def request(self, data: dict = None, url_params: dict = None, **opt):
		self.__set_request_url(url=opt.get('endpoint'), params=url_params)
		return self.__make_request(method=self._request_method, data=data, **opt)

	def __init__(self, url, **kwargs):
		self.__set_request_url(url=url, params={})
		if kwargs.get('auth_token'):
			self.__headers['Authorization'] = f"Bearer {kwargs.get('auth_token')}"

		if kwargs.get('method'):
			self._request_method = kwargs.get('method')

	def __str__(self):
		return f"<{self.__class__.__name__} {self._request_method.upper()} '{self._url}'>"

	def __set_request_url(self, url: str = None, params: dict = None):
		params_list = params.values() if isinstance(params, dict) else []
		url = self._url if url is None else url
		self._url = f"{url}/{'/'.join([str(i) for i in params_list])}".rstrip('/')

	def __make_request(self, method='post', data: dict = None, **opt) -> dict:
		from requests import api
		data = dict() if data is None else data
		if opt.get('headers'):
			self.__headers = dict(**self.__headers, **opt.get('headers'))

		api_response = api.request(url=self._url, method=method, data=data, headers=self.__headers)

		if api_response.headers.get('Content-Type') == "application/json":
			return api_response.json()
		return dict(body=api_response.content.decode())
