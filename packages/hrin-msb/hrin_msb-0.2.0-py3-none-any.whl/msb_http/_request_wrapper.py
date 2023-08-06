from __future__ import annotations

from dataclasses import dataclass
from typing import Union
from rest_framework import request as drf_request


@dataclass
class RequestWrapper:
	request: Union[drf_request.Request] = None

	@property
	def __meta(self) -> dict:
		return self.request.META or {}

	@property
	def __headers(self) -> dict:
		return self.request.headers or {}

	def get(self, key: str = None, default=None):
		val = self.request.META
		return val if val is not None else default

	@property
	def cookie(self):
		return self.__meta.get('HTTP_COOKIE')

	@property
	def path(self) -> str:
		return self.__meta.get('PATH_INFO')

	@property
	def ip(self):
		return self.__meta.get('REMOTE_ADDR')

	@property
	def method(self) -> str:
		return self.__meta.get('REQUEST_METHOD')

	@property
	def script(self) -> str:
		return self.__meta.get('SCRIPT_NAME')

	@property
	def server(self) -> str:
		return self.__meta.get('SERVER_NAME')

	@property
	def port(self) -> int:
		return int(self.__meta.get('SERVER_PORT'))

	@property
	def protocol(self) -> str:
		return self.__meta.get('SERVER_PROTOCOL')

	@property
	def content_type(self) -> str:
		return self.__meta.get('CONTENT_TYPE')

	@property
	def query_string(self) -> str:
		return self.__meta.get('QUERY_STRING')

	@property
	def authorization(self) -> str:
		return self.__meta.get('HTTP_AUTHORIZATION')

	@property
	def user_agent(self) -> str:
		return self.__headers.get('User-Agent')
