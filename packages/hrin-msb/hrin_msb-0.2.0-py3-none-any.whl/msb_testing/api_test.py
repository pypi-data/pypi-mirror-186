from os import environ

from rest_framework.test import APILiveServerTestCase

from ._core import (ApiTestResult, TestConfig, LiveServerThreadWithReuse)


class ApiTest(APILiveServerTestCase):
	databases = '__all__'
	port = 8000
	server_thread_class = LiveServerThreadWithReuse

	__auth_tokens: dict = dict()
	_api_endpoints: dict = {}

	fixtures = None

	def _load_fixtures(self):
		if type(self.fixtures) in [list, tuple] and len(self.fixtures) > 0:
			from django.core import management
			management.call_command('loaddata', *self.fixtures)

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self._load_fixtures()

	def url(self, name: str):
		return self._api_endpoints.get(name)

	def setUp(self) -> None:
		self._authenticate(self.config.auth_credentials)

	@property
	def config(self):
		return TestConfig()

	@property
	def access_token(self):
		return self.__auth_tokens.get('access')

	@property
	def is_authenticated(self):
		return self.access_token not in ['', None]

	@property
	def api_test_result(self):
		return ApiTestResult

	def __log_api_request(self, **kwargs):
		if environ.get('ENVIRONMENT') == 'local':
			logstr = "{sep}Request: {method} {url}\nPayload: {data}\nOptions: {opt}\nResponse: {result}\n{sep}".format(
				sep=f"{'=' * 100}\n", method=kwargs.get('method').upper(), url=kwargs.get('request_url'),
				data=kwargs.get('data'), result=kwargs.get('response'), opt=kwargs.get('opt')
			)
			print(logstr)

	def __make_api_request(self, method='post', endpoint: str = '', data: dict | list = None, _func=None,
	                       **opt) -> ApiTestResult:
		data = dict() if data is None else data
		result = dict()
		try:
			extra_headers = opt.get('headers') if isinstance(opt.get('headers'), dict) else {}
			request_headers = {**self.config.default_headers, **extra_headers}
			request_url = self.config.make_url(endpoint=endpoint)

			if self.access_token:
				self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

			handler_func = _func if callable(_func) else self.client.post
			api_response = handler_func(request_url, data, 'json', **request_headers)

			if api_response.headers.get('Content-Type') == self.config.request_content_type:
				result = api_response.json()
			else:
				result = dict(body=api_response.getvalue())
		except Exception as e:
			pass
		finally:
			self.__log_api_request(method=method, request_url=request_url, data=data, opt=opt, response=result)
			result = ApiTestResult(**result)

		# return only the data section of the api response, unless specifically asked for
		return result

	def _authenticate(self, auth_credentials: dict | list = None) -> None:
		if self.is_authenticated:
			return
		auth_result = self.api_post(self.config.auth_url, payload=auth_credentials)
		if self.assertEquals(list(auth_result.data.keys()), ['refresh', 'access']):
			self.__auth_tokens = dict(auth_result.data)

	def api_get(self, endpoint: str = '', payload: dict | list = None, **opt) -> ApiTestResult:
		return self.__make_api_request('get', endpoint, payload, _func=self.client.get, **opt)

	def api_post(self, endpoint: str = '', payload: dict | list = None, **opt) -> ApiTestResult:
		return self.__make_api_request('post', endpoint, payload, _func=self.client.post, **opt)

	def api_put(self, endpoint: str = '', payload: dict | list = None, **opt) -> ApiTestResult:
		return self.__make_api_request('put', endpoint, payload, _func=self.client.put, **opt)

	def api_delete(self, endpoint: str = '', payload: dict = None, **opt) -> ApiTestResult:
		return self.__make_api_request('delete', endpoint, payload, _func=self.client.delete, **opt)
